
import json
import sys
from opportunity_scanner import find_event_triggers
from event_extractor import extract_events_from_screens

def main():
    if len(sys.argv) != 4:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory> <path_to_screens.rpy> <event_id_to_debug>", file=sys.stderr)
        sys.exit(1)

    game_dir = sys.argv[2]
    screens_rpy_path = sys.argv[1]
    event_to_debug = sys.argv[3]

    print(f"--- [DEBUG] Loading master event list from '{screens_rpy_path}' ---", file=sys.stderr)
    master_event_list = extract_events_from_screens(screens_rpy_path)
    if not master_event_list:
        print("Could not extract master event list. Halting.", file=sys.stderr)
        return

    if event_to_debug not in master_event_list:
        print(f"Error: Event ID '{event_to_debug}' not found in the master event list.", file=sys.stderr)
        return

    print(f"--- [DEBUG] Scanning all scripts to find triggers... ---", file=sys.stderr)
    event_triggers = find_event_triggers(game_dir, master_event_list)
    
    print("\n" + "="*50, file=sys.stderr)
    print(f"--- [DEBUG] RESULT FOR '{event_to_debug}' ---", file=sys.stderr)
    print("="*50, file=sys.stderr)


    if event_to_debug in event_triggers:
        condition = event_triggers[event_to_debug]
        print(f"Found Condition: \"{condition}\"")
    else:
        print("No direct 'if -> jump' trigger was found for this event.")
        print("It might be triggered by a menu choice, a call from another label, or a custom condition.")

if __name__ == "__main__":
    main()