import json
import operator
import sys
import copy
import os

# --- MODIFIED: GameState now manages the core game loop variables ---
class GameState:
    def __init__(self):
        self.variables = {}
        # Core simulation state
        self.totaldays = 1
        self.day = 1 # Day of the week (1=Mon, 2=Tue, etc.)
        self.time_of_day = "morning" # morning, afternoon, night
        self.current_hub_label = "mondaymorning"

    def __str__(self):
        state_summary = {
            "hub": self.current_hub_label,
            "day": self.day,
            "totaldays": self.totaldays,
            "time": self.time_of_day,
            "variables": self.variables
        }
        return json.dumps(state_summary, indent=2)

class EventAnalysisPacket:
    # (This class is unchanged)
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

# --- MODIFIED: Simulator is now a Game Loop Manager ---
class Simulator:
    def __init__(self, ast, output_dir="event_archive"):
        self.ast = ast
        self.game_state = GameState()
        self.labels = {n['name']: n for n in ast.get('children', []) if n.get('type') == 'label'}
        self.output_dir = output_dir
        if not os.path.exists(output_dir): os.makedirs(output_dir)

        self.operators = {"=": operator.setitem, "+=": operator.iadd, "-=": operator.isub}
        self.comparisons = {">": operator.gt, "<": operator.lt, "==": operator.eq, "!=": operator.ne, ">=": operator.ge, "<=": operator.le}

        self.call_stack = []
        self.total_events_run = 0

        print(f"Simulator (V12 - Game Loop Manager) initialized. Found {len(self.labels)} labels.", file=sys.stderr)
        self._initialize_renpy_defaults()

    def _initialize_renpy_defaults(self):
        print("--- Initializing Ren'Py Default Variables ---", file=sys.stderr)
        init_blocks = sorted([n for n in self.ast.get('children', []) if n.get('type') == 'init_block'], key=lambda x: x.get('priority', 0))
        for block in init_blocks:
            self.execute_node_list(block.get('children', []), None)
        print("--- Ren'Py Defaults Initialized ---", file=sys.stderr)

    # --- NEW: Sets up the state for a new game ---
    def set_initial_state(self, new_game_variables):
        """
        Sets the initial state of the game, including player-defined
        variables and the starting day/time.
        """
        self.game_state.variables = new_game_variables
        self.game_state.totaldays = self.game_state.variables.get("totaldays", 1)
        self.game_state.day = self.game_state.variables.get("day", 1)
        self.game_state.time_of_day = "morning"
        self._update_hub_label() # Calculate the first hub label
        print(f"--- Simulator state initialized. Starting at: {self.game_state.current_hub_label} ---", file=sys.stderr)

    # --- NEW: Public method for the controller to get the current location ---
    def get_current_hub(self):
        return self.game_state.current_hub_label

    # --- NEW: Main entry point for the controller to execute a player's choice ---
    def execute_player_choice(self, choice_label):
        """
        Executes an event chain starting from a given label and then
        advances the game's time.
        """
        # --- ADD THIS CHECK ---
        if choice_label is None:
            print(f"\n--- [SIM] No choice made. Passing time. ---", file=sys.stderr)
            self._advance_time()
            print(f"--- [SIM] Time advanced. New hub is: '{self.game_state.current_hub_label}' ---", file=sys.stderr)
            return
        # --- END OF ADDITION ---

        print(f"\n--- [SIM] Player chose '{choice_label}'. Executing event chain. ---", file=sys.stderr)
        self._run_event_chain(choice_label)
        self._advance_time()
        print(f"--- [SIM] Time advanced. New hub is: '{self.game_state.current_hub_label}' ---", file=sys.stderr)



    # --- NEW: Private method to handle time and day progression ---
    def _advance_time(self):
        if self.game_state.time_of_day == "morning":
            self.game_state.time_of_day = "afternoon"
        elif self.game_state.time_of_day == "afternoon":
            self.game_state.time_of_day = "night"
        elif self.game_state.time_of_day == "night":
            self.game_state.time_of_day = "morning"
            self.game_state.day = (self.game_state.day % 7) + 1 # Cycle 1-7
            self.game_state.totaldays += 1
            # Update the persistent variables
            self.game_state.variables["day"] = self.game_state.day
            self.game_state.variables["totaldays"] = self.game_state.totaldays

        self._update_hub_label()

    # --- NEW: Private method to calculate the current hub label from the state ---
    def _update_hub_label(self):
        day_map = {
            1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday",
            5: "friday", 6: "saturday", 7: "sunday"
        }
        day_name = day_map.get(self.game_state.day, "monday")
        self.game_state.current_hub_label = f"{day_name}{self.game_state.time_of_day}"

    def _evaluate_value(self, val_str):
        # (This method is unchanged)
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
        # (This method is unchanged)
        for op, func in self.comparisons.items():
            if op in cond_str:
                parts = [p.strip() for p in cond_str.split(op, 1)]
                left, right = self._evaluate_value(parts[0]), self._evaluate_value(parts[1])
                if left is None or right is None: return False
                return func(left, right)
        bool_val = self._evaluate_value(cond_str)
        return bool(bool_val) if isinstance(bool_val, bool) else False

    def _execute_variable_assignment(self, node):
        # (This method is unchanged)
        expr = node.get('expression', '').lstrip('$').strip()
        op = next((o for o in self.operators if o in expr), None)
        if not op: return
        var, val_str = [p.strip() for p in expr.split(op, 1)]
        val = self._evaluate_value(val_str)
        if val is None: return
        if op == "=": self.game_state.variables[var] = val
        else: self.game_state.variables[var] = self.operators[op](self.game_state.variables.get(var, 0), val)

    def execute_node(self, node, packet):
        # (This method is unchanged)
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
            # NOTE: The player agent now handles menu choices. The simulator
            # will just pick the first option to ensure event chains complete.
            for choice in node.get('children', []):
                return self.execute_node_list(choice.get('children', []), packet)
        elif ntype == 'command':
            keyword, args = node.get('keyword'), node.get('args')
            if keyword == 'jump': return ('jump', args)
            if keyword == 'return': return ('return', None)
            if keyword == 'call':
                self.call_stack.append(None)
                return ('jump', args)
        return None

    def execute_node_list(self, nodes, packet):
        # (This method is unchanged)
        for node in nodes:
            signal = self.execute_node(node, packet)
            if signal: return signal
        return None

    def _handle_ai_handoff(self, packet):
        # (This method is unchanged)
        filename = f"{str(packet.event_id).zfill(4)}_{packet.label_name}.json"
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(packet.to_dict(), f, indent=2)
        print(f"--> [SIM] Event packet {packet.event_id} saved to {filepath}", file=sys.stderr)

    # --- RENAMED: from run_from_label to _run_event_chain to reflect its new internal role ---
    def _run_event_chain(self, start_label, max_jumps=50):
        current_label = start_label
        jumps = 0
        while current_label and current_label in self.labels and jumps < max_jumps:
            self.total_events_run += 1
            jumps += 1
            print(f"[SIM - Event {self.total_events_run}: Executing '{current_label}']", file=sys.stderr)

            packet = EventAnalysisPacket(current_label, self.total_events_run)
            packet.set_initial_state(self.game_state.variables)

            signal = self.execute_node_list(self.labels[current_label].get('children', []), packet)

            packet.finalize(self.game_state.variables)
            self._handle_ai_handoff(packet)

            next_label = None
            if signal:
                stype, sval = signal
                if stype == 'jump': next_label = sval
                elif stype == 'return':
                    if self.call_stack: self.call_stack.pop(); break
                    else: break

            current_label = next_label
        if jumps >= max_jumps:
            print(f"[SIM] WARNING: Exceeded max jumps ({max_jumps}) in event chain starting from '{start_label}'. Halting chain.", file=sys.stderr)

# --- The main function is now just a placeholder for direct testing ---
def main():
    print("This script is now intended to be driven by completionist_controller.py.", file=sys.stderr)
    print("To test, you would load an AST, initialize the simulator, and call its methods.", file=sys.stderr)

if __name__ == "__main__":
    main()