import json
import operator
import sys
import copy
import os

class GameState:
    """Manages the state of all variables in the game."""
    def __init__(self):
        self.variables = {}

    def __str__(self):
        return json.dumps(self.variables, indent=2)

class EventAnalysisPacket:
    """A structured container for all data related to a single game event (label)."""
    def __init__(self, label_name, initial_state, event_id):
        self.event_id = event_id
        self.label_name = label_name
        self.initial_state = copy.deepcopy(initial_state)
        self.final_state = None
        self.dialogue_log = []
        self.state_changes = {}

    def add_dialogue(self, character, text):
        self.dialogue_log.append({"character": character, "text": text})

    def finalize(self, final_state):
        self.final_state = copy.deepcopy(final_state)
        self._calculate_deltas()

    def _calculate_deltas(self):
        """Compares initial and final state to find what changed."""
        delta = {}
        all_keys = set(self.initial_state.keys()) | set(self.final_state.keys())
        for key in all_keys:
            initial_value = self.initial_state.get(key)
            final_value = self.final_state.get(key)
            if initial_value != final_value:
                delta[key] = {"from": initial_value, "to": final_value}
        self.state_changes = delta
    
    def to_dict(self):
        return {
            "event_id": self.event_id,
            "event_label": self.label_name,
            "dialogue": self.dialogue_log,
            "state_changes": self.state_changes
        }

class Simulator:
    """
    Executes an AST, captures event data, and hands it off for cognitive analysis.
    """
    def __init__(self, ast, output_dir="event_archive"):
        self.ast = ast
        self.game_state = GameState()
        self.labels = self._find_all_labels()
        self.output_dir = output_dir
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        self.operators = {"=": operator.setitem, "+=": operator.iadd, "-=": operator.isub}
        self.comparisons = {">": operator.gt, "<": operator.lt, "==": operator.eq, "!=": operator.ne, ">=": operator.ge, "<=": operator.le}
        
        print("Simulator (V8 - Production) initialized.")
        self._initialize_game_state()

    def _find_all_labels(self):
        return {node['name']: node for node in self.ast.get('children', []) if node.get('type') == 'label'}

    def _initialize_game_state(self):
        print("--- Initializing Game State ---")
        init_blocks = sorted([n for n in self.ast.get('children', []) if n.get('type') == 'init_block'], key=lambda x: x.get('priority', 0))
        for block in init_blocks:
            self.execute_node_list(block.get('children', []), None)
        print("--- Game State Initialized ---")

    def _evaluate_value(self, value_str):
        value_str = str(value_str).strip()
        if value_str == 'True': return True
        if value_str == 'False': return False
        if value_str.startswith('"') and value_str.endswith('"'): return value_str[1:-1]
        try: return int(value_str)
        except (ValueError, TypeError): pass
        try: return float(value_str)
        except (ValueError, TypeError): pass
        return self.game_state.variables.get(value_str)

    def _evaluate_condition(self, condition_str):
        for op_key, op_func in self.comparisons.items():
            if op_key in condition_str:
                parts = [p.strip() for p in condition_str.split(op_key, 1)]
                left_val, right_val = self._evaluate_value(parts[0]), self._evaluate_value(parts[1])
                if left_val is None or right_val is None: return False
                return op_func(left_val, right_val)
        bool_val = self._evaluate_value(condition_str)
        return bool_val if isinstance(bool_val, bool) else False

    def _execute_variable_assignment(self, node):
        expression = node.get('expression', '').lstrip('$').strip()
        op_key = next((op for op in self.operators if op in expression), None)
        if not op_key: return
        parts = [p.strip() for p in expression.split(op_key, 1)]
        variable_name, value_str = parts[0], parts[1]
        value = self._evaluate_value(value_str)
        if value is None: return
        if op_key == "=": self.game_state.variables[variable_name] = value
        elif op_key in ["+=", "-="]:
            current_val = self.game_state.variables.get(variable_name, 0)
            self.game_state.variables[variable_name] = self.operators[op_key](current_val, value)

    def execute_node(self, node, current_packet):
        node_type = node.get('type')
        if node_type == 'dialogue':
            if current_packet: current_packet.add_dialogue(node.get('character', 'narrator'), node.get('text'))
        elif node_type == 'variable_assignment': self._execute_variable_assignment(node)
        elif node_type == 'if_statement': return self.execute_node_list(self._get_if_branch(node), current_packet)
        elif node_type == 'menu':
            first_choice = node.get('children', [{}])[0]
            if first_choice and current_packet:
                current_packet.add_dialogue("player_choice", first_choice.get('text', 'Unknown Choice'))
            return self.execute_node_list(first_choice.get('children', []), current_packet)
        elif node_type == 'command':
            keyword = node.get('keyword')
            if keyword == 'jump': return ('jump', node.get('args'))
            if keyword == 'return': return ('return', None)
        return None

    def _get_if_branch(self, if_node):
        if self._evaluate_condition(if_node.get('condition', 'False')): return if_node.get('children', [])
        for elif_block in if_node.get('elif_blocks', []):
            if self._evaluate_condition(elif_block.get('condition', 'False')): return elif_block.get('children', [])
        return if_node.get('else_block', {}).get('children', [])

    def execute_node_list(self, nodes, current_packet):
        for node in nodes:
            control_signal = self.execute_node(node, current_packet)
            if control_signal: return control_signal
        return None

    def send_to_event_analyst(self, packet):
        """
        Placeholder for handing off the event packet to the Cognitive Core.
        Currently saves the packet to a local directory.
        """
        filename = f"{str(packet.event_id).zfill(4)}_{packet.label_name}.json"
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(packet.to_dict(), f, indent=2)
        print(f"--> Event packet saved to {filepath}")

    def run_from_label(self, start_label_name):
        current_label_name = start_label_name
        event_counter = 0

        while current_label_name and current_label_name in self.labels:
            event_counter += 1
            
            # --- Event Capture ---
            print(f"\n[EVENT {event_counter}: Executing '{current_label_name}']")
            event_packet = EventAnalysisPacket(current_label_name, self.game_state.variables, event_counter)
            
            label_node = self.labels[current_label_name]
            control_signal = self.execute_node_list(label_node.get('children', []), event_packet)
            
            event_packet.finalize(self.game_state.variables)
            # --- Handoff ---
            self.send_to_event_analyst(event_packet)

            next_label = None
            if control_signal:
                signal_type, signal_value = control_signal
                if signal_type == 'jump': next_label = signal_value
                else: break
            
            current_label_name = next_label
        
        print(f"\n--- Simulation finished after {event_counter} events. ---")

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_ast_json_file>", file=sys.stderr)
        sys.exit(1)
    ast_file_path = sys.argv[1]
    try:
        with open(ast_file_path, 'r') as f: ast = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: Could not load AST file '{ast_file_path}'. {e}", file=sys.stderr)
        return

    sim = Simulator(ast)
    sim.run_from_label('start')

if __name__ == "__main__":
    main()