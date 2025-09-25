# completionist_controller.py (V11 - Correctly Integrated with Sim V12)
import json
import sys
import os
from sim import Simulator
from game_analyzer import GameLogicEvaluator

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory>", file=sys.stderr); sys.exit(1)
    game_dir, ast_path, hub_map_path = sys.argv[1], "global_ast.json", "hub_map.json"
    try:
        with open(ast_path, 'r', encoding='utf-8') as f: ast = json.load(f)
        with open(hub_map_path, 'r', encoding='utf-8') as f: game_map = json.load(f)
    except Exception as e:
        print(f"Error loading data files: {e}", file=sys.stderr); return

    sim = Simulator(ast)
    # The V12 simulator has its own initial state method, we don't need to call a separate one.
    # It initializes itself. We will just ensure the 'bonus' variable is set.
    sim.game_state.variables['bonus'] = False
    
    current_location = "start"
    visited_choices = {}
    
    day_map = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    MAX_LOOPS = 200
    for i in range(MAX_LOOPS):
        
        node_type = "unknown"
        if current_location in game_map["hubs"]: node_type = "hub"
        elif current_location in game_map["dispatchers"]: node_type = "dispatcher"
        elif current_location in game_map["transitions"]: node_type = "transition"
        
        sim._run_event_chain(current_location, process_only_one=True)
        
        # --- THIS IS THE FIX ---
        # The variables live inside the sim's 'game_state' object.
        evaluator = GameLogicEvaluator(sim.game_state.variables)
        day_of_week = day_map.get(sim.game_state.variables.get("day"), "Unknown")
        total_days = sim.game_state.variables.get("totaldays", 0)
        # --- END OF FIX ---
        
        print(f"\n==================== LOOP {i+1} ({day_of_week}, Day {total_days}) ====================", file=sys.stderr)
        print(f"[CONTROLLER] Location Processed: '{current_location}'", file=sys.stderr)
        
        if node_type == "hub":
            hub_label = current_location
            choices_map = game_map["hubs"][hub_label]["choices"]
            if hub_label not in visited_choices:
                visited_choices[hub_label] = set()

            chosen_path = None
            chosen_choice_text = None
            for choice_text, path_data in choices_map.items():
                if choice_text in visited_choices[hub_label]:
                    continue

                conditions = path_data.get("conditions", ["True"])
                all_conditions_met = all(evaluator.evaluate_condition(c) for c in conditions)
                
                if all_conditions_met:
                    print(f"[CONTROLLER] Found valid, untried choice: '{choice_text}'", file=sys.stderr)
                    print(f"             (Conditions: '{' and '.join(conditions)}' -> True)", file=sys.stderr)
                    
                    visited_choices[hub_label].add(choice_text)
                    chosen_path = path_data
                    chosen_choice_text = choice_text
                    break
            
            if chosen_path:
                current_location = chosen_path["target"]
                print(f"[CONTROLLER] DECISION: Choosing '{chosen_choice_text}' -> Jumps to '{current_location}'", file=sys.stderr)
            else:
                print(f"[CONTROLLER] All available choices at hub '{hub_label}' have been exhausted. Halting.", file=sys.stderr)
                break
        
        elif node_type == "dispatcher":
            paths = game_map["dispatchers"][current_location]
            next_location_found = False
            for path in paths:
                if path["condition"] == "else" or evaluator.evaluate_condition(path["condition"]):
                    current_location = path["target"]
                    print(f"[CONTROLLER] At Dispatcher. Condition '{path['condition']}' is TRUE. Jumping to '{current_location}'.", file=sys.stderr)
                    next_location_found = True
                    break
            if not next_location_found:
                print("[CONTROLLER] No conditions met in dispatcher. Dead end. Halting.", file=sys.stderr)
                break
        
        elif node_type == "transition":
            destination = game_map["transitions"][current_location]
            print(f"[CONTROLLER] At Transition. Following map from '{current_location}' to '{destination}'.", file=sys.stderr)
            current_location = destination

        else:
            print(f"[CONTROLLER] Location '{current_location}' is not a hub, dispatcher, or transition. Halting.", file=sys.stderr)
            break
            
    print(f"\n--- [CONTROLLER] Simulation finished after {i+1} loops. ---", file=sys.stderr)

if __name__ == "__main__":
    main()