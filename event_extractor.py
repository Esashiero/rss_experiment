import json
import re
import sys
import os

def extract_events_from_screens(screens_rpy_path):
    """
    Parses a screens.rpy file to extract the master list of replayable events.
    """
    if not os.path.exists(screens_rpy_path):
        # Error messages should go to stderr
        print(f"Error: File not found at '{screens_rpy_path}'", file=sys.stderr)
        return {}

    try:
        with open(screens_rpy_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return {}

    events = {}
    current_event_group = None

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        if "use game_menu(_(" in stripped_line and (" Events" in stripped_line or " SCENES" in stripped_line):
            try:
                current_event_group = stripped_line.split('"')[1].replace(" Events", "").replace(" SCENES", "").capitalize()
            except IndexError:
                current_event_group = "Unknown"
            continue

        if not current_event_group:
            continue
        
        if stripped_line.startswith("textbutton _(\""):
            try:
                name = stripped_line.split('"')[1]
                name = name.replace("✓", "")
                name = re.sub(r"\(.*?\)", "", name)
                name = re.sub(r"\{.*?\}", "", name)
                name = name.strip()
            except IndexError:
                continue

            event_id = None
            if i + 2 < len(lines):
                action_line = lines[i+2].strip()
                if "action Replay" in action_line:
                    try:
                        event_id = action_line.split('"')[1]
                    except IndexError:
                        pass

            if event_id and name:
                events[event_id] = {
                    "id": event_id,
                    "name": name,
                    "group": current_event_group,
                }

    return events

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_screens.rpy>", file=sys.stderr)
        sys.exit(1)

    screens_path = sys.argv[1]
    
    # --- MODIFICATION: Print status messages to stderr ---
    print(f"--- Parsing Events from '{screens_path}' ---", file=sys.stderr)
    master_event_list = extract_events_from_screens(screens_path)

    if not master_event_list:
        print("\nCould not find any events. Please check the file path and content.", file=sys.stderr)
    else:
        print(f"\n--- Successfully extracted {len(master_event_list)} events ---", file=sys.stderr)
        print("Outputting clean JSON to stdout...", file=sys.stderr)
        
        # --- NO CHANGE HERE: This print goes to stdout, which is what we want to save ---
        print(json.dumps(master_event_list, indent=2))

if __name__ == "__main__":
    main()