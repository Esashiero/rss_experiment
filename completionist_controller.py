# completionist_controller.py (V12 - Strategic Agent, Integrated & Corrected)
import json
import sys
import re
from sim import Simulator
from game_analyzer import GameLogicEvaluator

# --- Configuration ---
TARGET_EVENT = "day220"
# --- End Configuration ---

class StrategicAgent:
    def __init__(self, game_map, rpy_code_path):
        print("[AGENT] Initializing Strategic Agent...")
        self.game_map = game_map
        self.rpy_code_path = rpy_code_path
        self.target_event = TARGET_EVENT
        print(f"[AGENT] Target event set to: '{self.target_event}'")
        self.target_location, self.target_condition_string = self._find_target_info()
        print(f"[AGENT] Found target at label '{self.target_location}' with condition: {self.target_condition_string}")
        self.dependency_map = self._parse_v11check_dependencies()
        print(f"[AGENT] Parsed 'v11check'. Found {len(self.dependency_map)} point categories.")
        self.master_checklist = self._build_master_checklist()
        print(f"[AGENT] Built master checklist. Goal is to complete {len(self.master_checklist)} prerequisite events.")

    def _find_target_info(self):
        for hub_name, hub_data in self.game_map.get("hubs", {}).items():
            for path_data in hub_data.get("conditional_paths", []):
                if path_data["target"] == self.target_event:
                    return hub_name, path_data["condition"]
        raise ValueError(f"Target event '{self.target_event}' not found in hub_map.json conditional paths.")

    def _parse_v11check_dependencies(self):
        try:
            with open(self.rpy_code_path, 'r', encoding='utf-8-sig') as f: content = f.read()
        except FileNotFoundError: print(f"FATAL: RPY file '{self.rpy_code_path}' not found.", file=sys.stderr); sys.exit(1)
        # --- CORRECTED REGEX: Looks for 'label v11check:' instead of 'def v11check():' ---
        func_match = re.search(r'label\s+v11check\s*:(.*?)return', content, re.DOTALL)
        if not func_match: raise ValueError("Could not find 'label v11check:' in RPY file.")
        func_body = func_match.group(1); lines = [line.strip() for line in func_body.split('\n')]
        dependency_map = {}
        event_var_pattern = re.compile(r'^if\s+([a-zA-Z0-9_]+)\s*==\s*True:')
        point_var_pattern = re.compile(r'^\$\s*([a-zA-Z0-9_]+point)\s*\+=\s*1')
        for i, line in enumerate(lines):
            event_match = event_var_pattern.match(line)
            if event_match and i + 1 < len(lines):
                event_name, next_line = event_match.group(1), lines[i+1]
                point_match = point_var_pattern.match(next_line)
                if point_match:
                    point_name = point_match.group(1)
                    if point_name not in dependency_map: dependency_map[point_name] = []
                    dependency_map[point_name].append(event_name)
        return dependency_map

    def _build_master_checklist(self):
        point_req_pattern = re.compile(r'([a-zA-Z0-9_]+point)\s*>=\s*([0-9]+)')
        target_requirements = {m.group(1): int(m.group(2)) for m in point_req_pattern.finditer(self.target_condition_string)}
        master_checklist = set()
        for point_var, _ in target_requirements.items():
            if point_var in self.dependency_map: master_checklist.update(self.dependency_map[point_var])
        return master_checklist

    def choose_action(self, current_location, sim, visited_choices):
        # --- CORRECTED STATE READING for evaluator ---
        evaluator = GameLogicEvaluator(sim.game_state.variables)
        hub_label, choices_map = current_location, self.game_map["hubs"][current_location]["choices"]
        if hub_label not in visited_choices: visited_choices[hub_label] = set()
        possible_choices = [(txt, path) for txt, path in choices_map.items() if all(evaluator.evaluate_condition(c) for c in path.get("conditions", ["True"]))]
        
        # Priority 1: Strategic choice
        for choice_text, path_data in possible_choices:
            target_event = path_data["target"]
            # Assume event variable is the same as the label, or a known mapping
            if target_event in self.master_checklist and not sim.game_state.variables.get(target_event, False):
                visited_choices[hub_label].add(choice_text)
                return path_data["target"], choice_text, "STRATEGIC"
        # Priority 2: Exploratory choice
        for choice_text, path_data in possible_choices:
            if choice_text not in visited_choices[hub_label]:
                visited_choices[hub_label].add(choice_text)
                return path_data["target"], choice_text, "EXPLORATORY"
        return None, None, "STUCK"
        
# Replace the ENTIRE main() function with this DEBUG version
def main():
    print("DEBUG: Controller script started.", file=sys.stderr) # PROBE 1

    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <game_dir> <path_to_merged_rpy_file>", file=sys.stderr)
        sys.exit(1)
    
    game_dir, rpy_file_path = sys.argv[1], sys.argv[2]
    ast_path, hub_map_path = "global_ast.json", "hub_map.json"
    
    print(f"DEBUG: Attempting to load '{ast_path}' and '{hub_map_path}'.", file=sys.stderr) # PROBE 2
    
    try:
        with open(ast_path, 'r', encoding='utf-8') as f:
            ast = json.load(f)
        print(f"DEBUG: Successfully loaded '{ast_path}'.", file=sys.stderr) # PROBE 3

        with open(hub_map_path, 'r', encoding='utf-8') as f:
            game_map = json.load(f)
        print(f"DEBUG: Successfully loaded '{hub_map_path}'.", file=sys.stderr) # PROBE 4

    except Exception as e:
        print(f"DEBUG: FATAL ERROR during file loading: {e}", file=sys.stderr) # PROBE 5
        return # This is the silent exit point.

    # --- The rest of the main function is unchanged ---
    agent = StrategicAgent(game_map, rpy_file_path)
    sim = Simulator(ast)
    sim.set_initial_state({"totaldays": 1, "day": 1, "bonus": False})
    visited_choices = {}
    day_map = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
    MAX_LOOPS = 500
    for i in range(MAX_LOOPS):
        current_location = sim.get_current_hub()
        day_of_week = day_map.get(sim.game_state.day, "?")
        total_days = sim.game_state.totaldays
        time_of_day = sim.game_state.time_of_day
        print(f"\n===== LOOP {i+1} ({day_of_week}, Day {total_days} - {time_of_day}) =====", file=sys.stderr)
        print(f"[CONTROLLER] Current Hub: '{current_location}'", file=sys.stderr)
        if current_location in game_map.get("hubs", {}):
            next_event_label, choice_txt, choice_type = agent.choose_action(current_location, sim, visited_choices)
            if next_event_label:
                print(f"[CONTROLLER] DECISION ({choice_type}): '{choice_txt}' -> '{next_event_label}'", file=sys.stderr)
                sim.execute_player_choice(next_event_label)
            else:
                print(f"[CONTROLLER] STUCK/PASS: No strategic/exploratory choices left at '{current_location}'. Passing time.", file=sys.stderr)
                sim.execute_player_choice(None)
        else:
            print(f"[CONTROLLER] Non-hub location. Passing time.", file=sys.stderr)
            sim.execute_player_choice(None)
    print(f"\n--- Simulation finished after {i+1} loops. ---", file=sys.stderr)
