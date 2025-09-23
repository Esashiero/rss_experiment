
import json
import sys
import os
import re
import operator
from collections import defaultdict

class GameLogicEvaluator:
    """
    An upgraded utility class to safely evaluate complex game conditions.
    
    This version replaces the manual parser with Python's built-in `eval()`
    function, executed in a secure, sandboxed environment. This allows it
    to handle complex conditions (e.g., with '.lower()' or 'in') that the
    previous version could not.
    """
    def __init__(self, game_state):
        # The context provides the variables for the evaluation.
        # We use a defaultdict that returns `False` for any variable not
        # present in the game state. This mimics Ren'Py's behavior where
        # undefined variables are treated as None (which is falsy).
        self.context = defaultdict(lambda: False, game_state)

        # The globals dictionary is strictly limited for security.
        # By providing an empty __builtins__, we prevent the evaluated
        # code from accessing dangerous functions like `open()` or `__import__()`.
        self.secure_globals = {"__builtins__": {}}

    def evaluate_condition(self, cond_str):
        """
        Safely evaluates a condition string using the sandboxed `eval`.
        """
        if not cond_str:
            return True
            
        try:
            # We evaluate the condition string.
            # `secure_globals` prevents access to unsafe built-ins.
            # `self.context` provides the game state variables.
            result = eval(cond_str, self.secure_globals, self.context)
            return bool(result)
        except Exception as e:
            # Any error during evaluation (e.g., SyntaxError for a malformed
            # condition, TypeError for comparing incompatible types, or
            # AttributeError for calling a method on a non-existent variable)
            # means the condition is not met.
            # print(f"DEBUG: Could not evaluate '{cond_str}'. Error: {e}", file=sys.stderr)
            return False

def find_event_triggers(game_dir, master_event_list):
    """
    Scans all .rpy files to find the 'if' conditions that trigger known events.
    (This function is unchanged)
    """
    event_conditions = {}
    script_files = [os.path.join(root, f) for root, _, files in os.walk(game_dir) for f in files if f.endswith(".rpy")]

    print(f"\nScanning {len(script_files)} .rpy files for event triggers...", file=sys.stderr)

    for script_file in script_files:
        try:
            with open(script_file, 'r', encoding='utf-8-sig') as f:
                lines = [line.strip() for line in f.readlines()]
        except Exception:
            continue

        for i, line in enumerate(lines):
            if line.startswith("jump "):
                target_label = line.split(" ")[1]
                if target_label in master_event_list:
                    for j in range(1, 10):
                        if i - j < 0: break
                        prev_line = lines[i - j]
                        if prev_line.startswith("if "):
                            condition = prev_line[3:-1].strip()
                            event_conditions[target_label] = condition
                            break
    
    # --- Inside opportunity_scanner.py ---

    custom_conditions = {
        "aminew1": "totaldays >= 44 and amisroom10 and day24 and not aminew1",
        
        # --- ADD THIS NEW LINE ---
        "chikainvite1": "detention and chikainvite1 == False",
        "mollyfirsthall": "day271 and mollyfirsthall == False"
    }
    

    print(f"Found {len(event_conditions)} triggers via parsing.", file=sys.stderr)
    print(f"Applying {len(custom_conditions)} custom-defined triggers.", file=sys.stderr)
    
    event_conditions.update(custom_conditions)
    return event_conditions


def main():
    # (This function is unchanged)
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory> <path_to_events.json>", file=sys.stderr)
        sys.exit(1)
    
    game_dir = sys.argv[1]
    events_json_path = sys.argv[2]

    try:
        with open(events_json_path, 'r') as f:
            master_event_list = json.load(f)
        print(f"Successfully loaded {len(master_event_list)} events from '{events_json_path}'", file=sys.stderr)
    except Exception as e:
        print(f"Error loading event list file: {e}", file=sys.stderr)
        return

    event_triggers = find_event_triggers(game_dir, master_event_list)

    sample_game_state = {
        "totaldays": 44,
        "amisroom10": True,
        "day24": True,
        "aminew1": False,
        "firsttimeamisroom": True,
        "chapthreeactive": False,
        "day288": True,
        "otohadorm1": False,
        "harukadate1": True,
        # Let's add 'gsbonus' to test the complex condition
        "gsbonus": "some other bonus",
        "kirin_lust": 10,
        "amifingered": False,
        "sara_lust": 5,
        "shrine40": False,
        "rainking": False
    }

    print("\n--- Scanning for Triggered Events ---", file=sys.stderr)
    print(f"Using sample game state: {json.dumps(sample_game_state, indent=2)}", file=sys.stderr)

    evaluator = GameLogicEvaluator(sample_game_state)
    triggered_events = []

    for event_id, condition in event_triggers.items():
        is_triggered = evaluator.evaluate_condition(condition)
        if is_triggered:
            triggered_events.append({
                "event_id": event_id,
                "event_name": master_event_list.get(event_id, {}).get("name", "Unknown Name"),
                "condition": condition
            })

    print("\n--- Found Triggered Forced Events ---")
    if triggered_events:
        for event in triggered_events:
            print(f"- Event '{event['event_name']}' ({event['event_id']}) is TRIGGERED.")
            print(f"  Condition: \"{event['condition']}\" is TRUE.")
    else:
        print("No forced events triggered with the current game state.")

if __name__ == "__main__":
    main()
