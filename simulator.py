import json
import operator
import sys
import copy
import os

class GameState:
    def __init__(self): self.variables = {}
    def __str__(self): return json.dumps(self.variables, indent=2)

class EventAnalysisPacket:
    def __init__(self, label_name, event_id):
        self.event_id = event_id
        self.label_name = label_name
        self.initial_state = {}
        self.final_state = {}
        self.dialogue_log = []
        self.state_changes = {}

    def set_initial_state(self, state): self.initial_state = copy.deepcopy(state)
    def add_dialogue(self, char, txt): self.dialogue_log.append({"character": char, "text": txt})
    def finalize(self, final_state):
        self.final_state = copy.deepcopy(final_state)
        self._calculate_deltas()

    def _calculate_deltas(self):
        delta = {}
        all_keys = set(self.initial_state.keys()) | set(self.final_state.keys())
        for key in all_keys:
            init_val, final_val = self.initial_state.get(key), self.final_state.get(key)
            if init_val != final_val: delta[key] = {"from": init_val, "to": final_val}
        self.state_changes = delta
    
    def to_dict(self):
        return {"event_id": self.event_id, "event_label": self.label_name, "dialogue": self.dialogue_log, "state_changes": self.state_changes}

class Simulator:
    def __init__(self, ast, output_dir="event_archive"):
        self.ast = ast
        self.game_state = GameState()
        self.labels = {n['name']: n for n in ast.get('children', []) if n.get('type') == 'label'}
        self.output_dir = output_dir
        if not os.path.exists(output_dir): os.makedirs(output_dir)
        
        self.operators = {"=": operator.setitem, "+=": operator.iadd, "-=": operator.isub}
        self.comparisons = {">": operator.gt, "<": operator.lt, "==": operator.eq, "!=": operator.ne, ">=": operator.ge, "<=": operator.le}
        
        # --- CALL STACK IMPLEMENTATION ---
        # A list to keep track of where to return to after a 'call'
        self.call_stack = []

        print(f"Simulator (V9 - Global) initialized. Found {len(self.labels)} labels.")
        self._initialize_game_state()

    def _initialize_game_state(self):
        print("--- Initializing Game State ---")
        init_blocks = sorted([n for n in self.ast.get('children', []) if n.get('type') == 'init_block'], key=lambda x: x.get('priority', 0))
        for block in init_blocks: self.execute_node_list(block.get('children', []), None)
        print("--- Game State Initialized ---")

    def _evaluate_value(self, val_str):
        val_str = str(val_str).strip()
        if val_str == 'True': return True
        if val_str == 'False': return False
        if val_str.startswith('"') and val_str.endswith('"'): return val_str[1:-1]
        try: return int(val_str)
        except (ValueError, TypeError): pass
        try: return float(val_str)
        except (ValueError, TypeError): pass
        return self.game_state.variables.get(val_str)

    def _evaluate_condition(self, cond_str):
        for op, func in self.comparisons.items():
            if op in cond_str:
                parts = [p.strip() for p in cond_str.split(op, 1)]
                left, right = self._evaluate_value(parts[0]), self._evaluate_value(parts[1])
                if left is None or right is None: return False
                return func(left, right)
        bool_val = self._evaluate_value(cond_str)
        return bool_val if isinstance(bool_val, bool) else False

    def _execute_variable_assignment(self, node):
        expr = node.get('expression', '').lstrip('$').strip()
        op = next((o for o in self.operators if o in expr), None)
        if not op: return
        var, val_str = [p.strip() for p in expr.split(op, 1)]
        val = self._evaluate_value(val_str)
        if val is None: return
        if op == "=": self.game_state.variables[var] = val
        else: self.game_state.variables[var] = self.operators[op](self.game_state.variables.get(var, 0), val)

    def execute_node(self, node, packet):
        ntype = node.get('type')
        if ntype == 'dialogue':
            if packet: packet.add_dialogue(node.get('character', 'narrator'), node.get('text'))
        elif ntype == 'variable_assignment': self._execute_variable_assignment(node)
        elif ntype == 'if_statement':
            if self._evaluate_condition(node.get('condition', 'False')):
                return self.execute_node_list(node.get('children', []), packet)
        elif ntype == 'elif_statement':
            if self._evaluate_condition(node.get('condition', 'False')):
                return self.execute_node_list(node.get('children', []), packet)
        elif ntype == 'else_statement':
             return self.execute_node_list(node.get('children', []), packet)
        elif ntype == 'menu':
            # Default strategy: Pick first available choice
            for choice in node.get('children', []):
                return self.execute_node_list(choice.get('children', []), packet)
        elif ntype == 'command':
            keyword, args = node.get('keyword'), node.get('args')
            if keyword == 'jump': return ('jump', args)
            if keyword == 'return': return ('return', None)
            # --- HANDLE CALL COMMAND ---
            if keyword == 'call':
                # The 'from' argument tells renpy where to store the return location
                # We can simplify by just using our own stack
                self.call_stack.append(None) # Placeholder for current label, more advanced version could store it
                return ('jump', args)
        return None

    def execute_node_list(self, nodes, packet):
        for node in nodes:
            signal = self.execute_node(node, packet)
            if signal: return signal
        return None

    def _handle_ai_handoff(self, packet):
        filename = f"{str(packet.event_id).zfill(4)}_{packet.label_name}.json"
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(packet.to_dict(), f, indent=2)
        print(f"--> Event packet saved to {filepath}")

    def run_from_label(self, start_label):
        current_label = start_label
        event_count = 0
        visited_labels = set()

        while current_label and current_label in self.labels:
            if current_label in visited_labels and not self.call_stack:
                print(f"Warning: Detected potential loop at '{current_label}'. Halting simulation.")
                break
            visited_labels.add(current_label)
            
            event_count += 1
            print(f"\n[EVENT {event_count}: Executing '{current_label}']")
            
            packet = EventAnalysisPacket(current_label, event_count)
            packet.set_initial_state(self.game_state.variables)
            
            signal = self.execute_node_list(self.labels[current_label].get('children', []), packet)
            
            packet.finalize(self.game_state.variables)
            self._handle_ai_handoff(packet)

            next_label = None
            if signal:
                stype, sval = signal
                if stype == 'jump': next_label = sval
                elif stype == 'return':
                    if self.call_stack:
                        # In a real engine, you'd return to the statement after 'call'.
                        # For our purpose, we just stop this branch.
                        # A more complex implementation would pop a return label from the stack.
                        self.call_stack.pop()
                        break 
                    else: break # End of simulation path
            
            current_label = next_label
        
        print(f"\n--- Simulation finished after {event_count} events. ---")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_global_ast.json>", file=sys.stderr)
        sys.exit(1)
    ast_path = sys.argv[1]
    try:
        with open(ast_path, 'r') as f: ast = json.load(f)
    except Exception as e:
        print(f"Error loading AST file: {e}", file=sys.stderr)
        return

    sim = Simulator(ast)
    sim.run_from_label('start')

if __name__ == "__main__":
    main()