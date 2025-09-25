

import os
import re
import sys
from collections import defaultdict

class GameStateAnalyzer:
    """
    A direct, faithful port of the multi-stage analysis pipeline from the
    Lessons-In-Love-Guide-Tool (game_data.py).

    This class is initialized once. It parses all game files to build a
    complete event dependency graph. Its only job is to provide a 100%
    accurate list of available events for a given game state.
    """
    def __init__(self, game_dir, master_event_list):
        print("--- [Game Analyzer] Initializing... This may take a moment. ---", file=sys.stderr)
        self.master_event_list = master_event_list
        self.events_data = {event_id: {"conditions": [], "required_events": []} for event_id in master_event_list}
        self._build_dependency_graph(game_dir)
        print("--- [Game Analyzer] Initialization Complete. Dependency graph built. ---", file=sys.stderr)

    def _build_dependency_graph(self, game_dir):
        """
        Executes the full, multi-stage parsing logic from game_data.py.
        """
        # --- Stage 1: Gather raw conditions from all sources ---
        
        # 1a: Simple backward scan
        script_files = [os.path.join(root, f) for root, _, files in os.walk(game_dir) for f in files if f.endswith(".rpy")]
        for script_file in script_files:
            try:
                with open(script_file, 'r', encoding='utf-8-sig') as f: lines = [l.strip() for l in f]
            except Exception: continue
            for i, line in enumerate(lines):
                if line.startswith("jump "):
                    target = line.split(" ")[1]
                    if target in self.events_data:
                        for j in range(1, 10):
                            if i - j < 0: break
                            if lines[i - j].startswith("if "):
                                self.events_data[target]["conditions"].append(lines[i - j][3:-1].strip())
                                break
        
        # 1b: Custom conditions (the ground truth for complex events)
        custom_conditions = {
            "iofirsthall": "day247", "utafirsthall": "day247", "yasufirsthall": "day304",
            "toukafirsthall": "day304", "toukastreets1": "day304", "ramen1": "day154",
            "tsuneyofirsthall": "day154", "otohafirsthall": "day288", "mollycafe1": "day154",
            "mollyfirsthall": "day154", "kirindate1": "soccer20", "kirinfirsthall": "day271",
            "nodokafirsthall": "day288", "norikofirsthall": "day271", "osakodojo1": "osakodate1",
            "harukafirstlust": "harukadate1", "harukalust10": "harukadate1", "day5": "totaldays >= 5",
            "secondbeach7": "kirin_lust < 20", "dormwartwo11": "amifingered == False",
            "bucketscene": "otohadorm1 == False", # This condition is simple, but its prerequisites are not.
            "aminew1": "totaldays >= 44 and amisroom10 and day24",
        }
        for event_id, condition in custom_conditions.items():
            if event_id in self.events_data:
                self.events_data[event_id]["conditions"].append(condition)

        # --- Stage 2: Process conditions to build the dependency graph ---
        # This is the crucial logic that was missing before.
        for event_id, data in self.events_data.items():
            processed_conditions = []
            raw_conditions = list(dict.fromkeys(data["conditions"])) # Deduplicate
            
            for cond_str in raw_conditions:
                # Split 'and' conditions to find all parts
                parts = [p.strip() for p in cond_str.replace("(", "").replace(")", "").split(" and ")]
                for part in parts:
                    # A simple variable name (like 'osakodate1') is a prerequisite event
                    variable = re.split(r'([<>=!]+)', part)[0].strip()
                    if variable in self.master_event_list and variable != event_id:
                        data["required_events"].append(variable)
                    else:
                        # If it's not another event, it's a regular condition
                        processed_conditions.append(part)
            
            # Store the cleaned, non-event conditions
            data["conditions"] = list(dict.fromkeys(processed_conditions))
            data["required_events"] = list(dict.fromkeys(data["required_events"]))

    def get_available_events(self, current_game_state):
        """
        Evaluates the pre-built dependency graph against the current game state.
        Returns a small, accurate list of truly available event IDs.
        """
        evaluator = GameLogicEvaluator(current_game_state)
        available_events = []

        for event_id, data in self.events_data.items():
            # Condition 1: The event itself must not be complete.
            if current_game_state.get(event_id, False):
                continue
            
            # Condition 2: All required prerequisite events must be complete.
            reqs_met = all(current_game_state.get(req, False) for req in data["required_events"])
            if not reqs_met:
                continue
            
            # Condition 3: All other simple conditions must evaluate to True.
            other_conds_met = all(evaluator.evaluate_condition(cond) for cond in data["conditions"])
            if not other_conds_met:
                continue

            # If all conditions pass, the event is truly available.
            available_events.append(event_id)
            
        return available_events

class GameLogicEvaluator:
    def __init__(self, game_state):
        self.context = defaultdict(lambda: False, game_state)
        self.secure_globals = {"__builtins__": {}}
    def evaluate_condition(self, cond_str):
        if not cond_str: return True
        try: return bool(eval(cond_str, self.secure_globals, self.context))
        except Exception: return False
