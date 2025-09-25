# completionist_controller.py (V13 - Full Integration with GameStateAnalyzer)
import json
import sys
import re
import os
from sim import Simulator
from game_analyzer import GameStateAnalyzer, GameLogicEvaluator # FIXED: Added GameLogicEvaluator
from event_extractor import extract_events_from_screens

# --- Configuration ---
TARGET_EVENT = "day220"
# --- End Configuration ---

class StrategicAgent:
    # FIXED: Corrected all indentation within this class
    def __init__(self, game_map, rpy_code_path, analyzer):
        print("[AGENT] Initializing Strategic Agent...")
        self.game_map = game_map
        self.rpy_code_path = rpy_code_path
        self.analyzer = analyzer
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
                if path_data.get("target") == self.target_event:
                    return hub_name, path_data["condition"]
        # Fallback for the AST-corrected map where the condition is "True"
        for hub_name, hub_data in self.game_map.get("hubs", {}).items():
            for path_data in hub_data.get("conditional_paths", []):
                 if path_data.get("target") == self.target_event and path_data.get("condition") == "True":
                     # We need to find the REAL condition from the rpy file now
                     with open(self.rpy_code_path, 'r', encoding='utf-8-sig') as f:
                         content = f.read()
                     # This regex is a bit of a guess, but it's our best shot
                     match = re.search(r'if\s+\(\(totaldays\s*>=.*?\s*jump\s+day220', content, re.DOTALL)
                     if match:
                         # Extract the condition part
                         condition_str = match.group(0).replace('jump day220', '').replace('if', '').strip()
                         if condition_str.endswith(':'): condition_str = condition_str[:-1]
                         return hub_name, condition_str
        raise ValueError(f"Target event '{self.target_event}' not found in hub_map.json conditional paths.")

    def _parse_v11check_dependencies(self):
        try:
            with open(self.rpy_code_path, 'r', encoding='utf-8-sig') as f: content = f.read()
        except FileNotFoundError: print(f"FATAL: RPY file '{self.rpy_code_path}' not found.", file=sys.stderr); sys.exit(1)
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
        evaluator = GameLogicEvaluator(sim.game_state.variables)
        hub_label = current_location
        choices_map = self.game_map["hubs"][hub_label]["choices"]

        if hub_label not in visited_choices:
            visited_choices[hub_label] = set()

        possible_choices = {
            txt: path for txt, path in choices_map.items() 
            if all(evaluator.evaluate_condition(c) for c in path.get("conditions", ["True"]))
        }

        available_events = self.analyzer.get_available_events(sim.game_state.variables)
        print(f"[AGENT] Analyzer reports {len(available_events)} events are available now.", file=sys.stderr)

        valid_strategic_choices = {}
        for choice_text, path_data in possible_choices.items():
            if path_data["target"] in available_events:
                if path_data["target"] in self.master_checklist:
                    # Make sure we haven't already completed this event
                    if not sim.game_state.variables.get(path_data["target"], False):
                        valid_strategic_choices[choice_text] = path_data

        if valid_strategic_choices:
            choice_text, path_data = list(valid_strategic_choices.items())[0]
            visited_choices[hub_label].add(choice_text)
            return path_data["target"], choice_text, "STRATEGIC"

        for choice_text, path_data in possible_choices.items():
            if choice_text not in visited_choices[hub_label]:
                visited_choices[hub_label].add(choice_text)
                return path_data["target"], choice_text, "EXPLORATORY"
                
        return None, None, "STUCK"
# In completionist_controller.py, replace the ENTIRE main() function with this new version.

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <game_dir> <path_to_merged_rpy_file>", file=sys.stderr)
        sys.exit(1)
    
    game_dir, rpy_file_path = sys.argv[1], sys.argv[2]
    ast_path, hub_map_path = "global_ast.json", "hub_map.json"
    screens_rpy_path = os.path.join(game_dir, "screens.rpy")

    try:
        with open(ast_path, 'r', encoding='utf-8') as f:
            ast = json.load(f)
        with open(hub_map_path, 'r', encoding='utf-8') as f:
            game_map = json.load(f)
    except Exception as e:
        print(f"Error loading data files: {e}", file=sys.stderr)
        return

    # --- Initialization (Unchanged) ---
    print("--- Initializing Game Analyzer ---", file=sys.stderr)
    master_event_list = extract_events_from_screens(screens_rpy_path)
    analyzer = GameStateAnalyzer(game_dir, master_event_list)
    print("--- Game Analyzer Initialized ---", file=sys.stderr)
    
    agent = StrategicAgent(game_map, rpy_file_path, analyzer)
    sim = Simulator(ast)
    sim.set_initial_state({"totaldays": 1, "day": 1, "bonus": False}) # Set defaults, intro will override

    # --- PHASE 1: RUN THE GAME INTRODUCTION ---
    print("\n===== EXECUTING GAME INTRODUCTION =====", file=sys.stderr)
    current_location = "start"
    
    # Keep running event chains until we land in a hub defined in our map
    while current_location and current_location not in game_map.get("hubs", {}):
        print(f"[CONTROLLER] Running intro sequence: '{current_location}'", file=sys.stderr)
        next_location = sim._run_event_chain(current_location)
        
        # Safety break to prevent infinite loops if something goes wrong
        if not next_location or next_location == current_location:
            print(f"[CONTROLLER] STUCK in intro at '{current_location}'. Halting.", file=sys.stderr)
            return
        
        current_location = next_location
    
    print(f"===== INTRODUCTION COMPLETE. First hub is '{current_location}' =====\n", file=sys.stderr)

    # --- PHASE 2: BEGIN THE MAIN STRATEGIC LOOP ---
    visited_choices = {}
    day_map = {1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat", 7: "Sun"}
    MAX_LOOPS = 50

    for i in range(MAX_LOOPS):
        # The simulator now correctly manages the current hub after the intro
        current_hub = sim.get_current_hub()
        
        day_of_week = day_map.get(sim.game_state.day, "?")
        total_days = sim.game_state.totaldays
        time_of_day = sim.game_state.time_of_day
        print(f"\n===== LOOP {i+1} ({day_of_week}, Day {total_days} - {time_of_day}) =====", file=sys.stderr)
        print(f"[CONTROLLER] Current Hub: '{current_hub}'", file=sys.stderr)
        
        if current_hub in game_map.get("hubs", {}):
            next_event_label, choice_txt, choice_type = agent.choose_action(current_hub, sim, visited_choices)
            if next_event_label:
                print(f"[CONTROLLER] DECISION ({choice_type}): '{choice_txt}' -> '{next_event_label}'", file=sys.stderr)
                sim.execute_player_choice(next_event_label)
            else:
                print(f"[CONTROLLER] STUCK/PASS: No choices left at '{current_hub}'. Passing time.", file=sys.stderr)
                sim.execute_player_choice(None)
        else:
            print(f"[CONTROLLER] Non-hub location '{current_hub}'. Passing time.", file=sys.stderr)
            sim.execute_player_choice(None)

        if i + 1 >= MAX_LOOPS:
             print(f"\n--- Simulation reached max loops ({MAX_LOOPS}). Halting. ---", file=sys.stderr)
             break

if __name__ == "__main__":
    main()
