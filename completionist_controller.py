
import json
import sys
import os
import re
from sim import Simulator
# --- MODIFICATION: Import from our new, accurate finder ---
from condition_finder import find_all_conditions
from event_extractor import extract_events_from_screens
# --- GameLogicEvaluator is now only needed here ---
from collections import defaultdict

class GameLogicEvaluator:
    def __init__(self, game_state):
        self.context = defaultdict(lambda: False, game_state)
        self.secure_globals = {"__builtins__": {}}
    def evaluate_condition(self, cond_str):
        if not cond_str: return True
        try:
            return bool(eval(cond_str, self.secure_globals, self.context))
        except Exception:
            return False

def create_new_game_state():
    return { "totaldays": 1, "day": 1, "money": 50 }

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory> <path_to_screens.rpy>", file=sys.stderr)
        sys.exit(1)

    game_dir = sys.argv[1]
    screens_rpy_path = sys.argv[2]
    
    print("--- [CONTROLLER] Setup Phase ---", file=sys.stderr)
    master_event_list = extract_events_from_screens(screens_rpy_path)
    print(f"Loaded {len(master_event_list)} total events.", file=sys.stderr)
    
    # --- MODIFICATION: Use the new, robust condition finder ---
    event_triggers = find_all_conditions(game_dir, master_event_list)

    print("\n--- [CONTROLLER] Simulation Phase ---", file=sys.stderr)
    ast_path = "global_ast.json"
    if not os.path.exists(ast_path):
        print(f"Error: Global AST file not found at '{ast_path}'.", file=sys.stderr)
        return
        
    with open(ast_path, 'r') as f: ast = json.load(f)
    sim = Simulator(ast)
    
    sim.game_state.variables = create_new_game_state()
    print(f"Initialized with New Game State: {json.dumps(sim.game_state.variables)}", file=sys.stderr)
    
    print("\n--- [CONTROLLER] Executing mandatory game start sequence from 'start' label ---", file=sys.stderr)
    if 'start' in sim.labels:
        sim.run_from_label('start')
        sim.game_state.variables['start'] = True
        print("--- [CONTROLLER] Game start sequence complete. Beginning completionist loop. ---", file=sys.stderr)
    
    MAX_EVENTS_TO_RUN = 100
    for i in range(1, MAX_EVENTS_TO_RUN + 1):
        print(f"\n--- [CONTROLLER] Loop {i} ---", file=sys.stderr)
        
        current_game_state = sim.game_state.variables
        evaluator = GameLogicEvaluator(current_game_state)
        
        available_events = []
        for event_id, condition in event_triggers.items():
            # No need to check completion flag here, it's now part of the condition string
            if evaluator.evaluate_condition(condition):
                available_events.append(event_id)

        if not available_events:
            print("--- [CONTROLLER] No more available events found. Simulation complete. ---", file=sys.stderr)
            break
        
        # --- MODIFICATION: No more prioritization needed! Just pick the first. ---
        # The list is now accurate.
        event_to_run = available_events[0]
        event_name = master_event_list.get(event_to_run, {}).get("name", "Unknown")

        print(f"Found {len(available_events)} available events. Choosing '{event_name}' ({event_to_run})'", file=sys.stderr)

        sim.run_from_label(event_to_run)
        print(f"--- [CONTROLLER] Forcing completion flag: '{event_to_run}' = True ---", file=sys.stderr)
        sim.game_state.variables[event_to_run] = True

    if i >= MAX_EVENTS_TO_RUN:
        print(f"--- [CONTROLLER] Reached max event limit of {MAX_EVENTS_TO_RUN}. Halting. ---", file=sys.stderr)

if __name__ == "__main__":
    main()
