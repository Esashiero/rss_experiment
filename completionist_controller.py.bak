
import json
import sys
import os
import re  # <-- THIS IS THE MISSING LINE THAT FIXES THE CRASH
from sim import Simulator
from opportunity_scanner import find_event_triggers, GameLogicEvaluator
from event_extractor import extract_events_from_screens

def create_new_game_state():
    """
    Returns a dictionary representing the state of a brand new game.
    This is crucial for ensuring the simulation starts correctly.
    """
    return {
        "totaldays": 1,
        "day": 1,
        "money": 50 
    }

def prioritize_events(available_events, event_triggers):
    """
    Scores and sorts available events to find the most logical one to run next.
    (Version 2 - More Nuanced)
    """
    scored_events = []
    for event_id in available_events:
        score = 0
        condition = event_triggers.get(event_id, "").lower()

        day_match = re.search(r'totaldays\s*(>=|==)\s*(\d+)', condition)
        if day_match:
            day_num = int(day_match.group(2))
            if day_num < 50:
                score += (1000 - day_num)

        if event_id.startswith('firsttime'):
            score += 500
            
        love_match = re.search(r'_love\s*(>=|==)\s*(\d+)', condition)
        if love_match:
            love_num = int(love_match.group(2))
            if love_num < 10:
                score += 100
        
        if "invite" in event_id:
            score -= 100
            
        scored_events.append((score, event_id))
    
    scored_events.sort(key=lambda x: x[0], reverse=True)
    
    print("--- Top 5 Prioritized Events ---", file=sys.stderr)
    for score, event_id in scored_events[:5]:
        print(f"  - Score {score}: {event_id}", file=sys.stderr)
    print("---------------------------------", file=sys.stderr)

    return [event_id for score, event_id in scored_events]

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory> <path_to_screens.rpy>", file=sys.stderr)
        sys.exit(1)

    game_dir = sys.argv[1]
    screens_rpy_path = sys.argv[2]
    
    print("--- [CONTROLLER] Setup Phase ---", file=sys.stderr)
    master_event_list = extract_events_from_screens(screens_rpy_path)
    print(f"Loaded {len(master_event_list)} total events.", file=sys.stderr)
    event_triggers = find_event_triggers(game_dir, master_event_list)
    print(f"Found {len(event_triggers)} trigger conditions for events.", file=sys.stderr)

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
            has_been_completed = current_game_state.get(event_id, False)
            if not has_been_completed and evaluator.evaluate_condition(condition):
                available_events.append(event_id)

        if not available_events:
            print("--- [CONTROLLER] No more available events found. Simulation complete. ---", file=sys.stderr)
            break
        
        sorted_events = prioritize_events(available_events, event_triggers)
        event_to_run = sorted_events[0]
        event_name = master_event_list.get(event_to_run, {}).get("name", "Unknown")

        print(f"Found {len(available_events)} available events. Prioritized choice is '{event_name}' ({event_to_run})'", file=sys.stderr)

        sim.run_from_label(event_to_run)
        print(f"--- [CONTROLLER] Forcing completion flag: '{event_to_run}' = True ---", file=sys.stderr)
        sim.game_state.variables[event_to_run] = True

    if i >= MAX_EVENTS_TO_RUN:
        print(f"--- [CONTROLLER] Reached max event limit of {MAX_EVENTS_TO_RUN}. Halting. ---", file=sys.stderr)

if __name__ == "__main__":
    main()
