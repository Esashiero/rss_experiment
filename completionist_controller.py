# completionist_controller.py

import json
import sys
import os
from sim import Simulator
from hub_analyzer import get_hub_choices # <-- NEW: Import the hub analyzer
# Note: GameStateAnalyzer is no longer needed for driving the main loop,
# but could be used later for more complex logic or verification.

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory>", file=sys.stderr)
        sys.exit(1)

    game_dir = sys.argv[1]
    ast_path = "global_ast.json"

    if not os.path.exists(ast_path):
        print(f"Error: Global AST file not found at '{ast_path}'. Please generate it first using the parser.", file=sys.stderr)
        return

    print("--- [CONTROLLER] Setup Phase ---", file=sys.stderr)
    try:
        with open(ast_path, 'r') as f:
            ast = json.load(f)
    except Exception as e:
        print(f"Error loading or parsing AST file: {e}", file=sys.stderr)
        return

    # --- Initialize the new Simulator ---
    sim = Simulator(ast)

    # --- Create a new game state and run the mandatory 'start' sequence ---
    # This gets the game to the first real day.
    initial_vars = {"totaldays": 1, "day": 1, "money": 50}
    sim.set_initial_state(initial_vars)
    print("\n--- [CONTROLLER] Executing mandatory game start sequence from 'start' label ---", file=sys.stderr)
    sim.execute_player_choice('start') # This will run 'start' and then advance time to the next hub

    print("\n--- [CONTROLLER] Game start complete. Beginning Hub-and-Spoke simulation loop. ---", file=sys.stderr)

    # --- The New Simulation Loop ---
    MAX_DAYS_TO_SIMULATE = 5 # Let's simulate 5 full days
    while sim.game_state.totaldays <= MAX_DAYS_TO_SIMULATE:
        current_hub = sim.get_current_hub()
        print(f"\n========================================================", file=sys.stderr)
        print(f"   CONTROLLER LOOP: Day {sim.game_state.totaldays}, {sim.game_state.time_of_day.upper()}", file=sys.stderr)
        print(f"========================================================", file=sys.stderr)
        print(f"[CONTROLLER] Current Hub: '{current_hub}'", file=sys.stderr)


        # 1. PERCEIVE: Use the Hub Analyzer to see what choices are available.
        available_choices = get_hub_choices(ast, current_hub)
        print(f"[CONTROLLER] Found {len(available_choices)} choices in hub: {[c['text'] for c in available_choices]}", file=sys.stderr)

        # 2. DECIDE: Choose an action.
        # For a completionist, the simplest strategy is to always pick the first valid option.
        if not available_choices:
            print("[CONTROLLER] No choices found in hub. Passing time.", file=sys.stderr)
            # We tell the simulator to execute nothing, which will just advance time.
            choice_to_execute = None
        else:
            # Simple Strategy: Always pick the first choice.
            chosen_action = available_choices[0]
            choice_to_execute = chosen_action['target_label']
            print(f"[CONTROLLER] DECISION: Choosing '{chosen_action['text']}' -> jumps to '{choice_to_execute}'", file=sys.stderr)

        # 3. ACT: Command the simulator to execute the choice.
        # The simulator will run the corresponding event chain and advance time automatically.
        sim.execute_player_choice(choice_to_execute)

    print(f"\n--- [CONTROLLER] Simulation finished after reaching Day {MAX_DAYS_TO_SIMULATE}. ---", file=sys.stderr)


if __name__ == "__main__":
    main()