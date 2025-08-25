import json
import re # We need the 're' module

class GameState:
    """A class to hold the state of the game's variables."""
    def __init__(self):
        self.variables = {}
        print("GameState initialized.")

    # --- NO CHANGES IN THIS CLASS ---
    def set_variable(self, name, value):
        clean_name = name.strip().lstrip('$').strip()
        self.variables[clean_name] = value
        print(f"STATE_UPDATE: {clean_name} = {value}")

    def get_variable(self, name):
        clean_name = name.strip().lstrip('$').strip()
        return self.variables.get(clean_name)

class Simulator:
    """
    The main engine that traverses the AST and simulates the game's state.
    """
    def __init__(self, ast):
        self.ast = ast
        self.game_state = GameState()
        self.labels = self._find_all_labels()
        print("Simulator initialized.")

    def _find_all_labels(self):
        # --- NO CHANGES IN THIS METHOD ---
        label_map = {}
        for node in self.ast['children']:
            if node['type'] == 'label':
                label_map[node['name']] = node
        print(f"Found labels: {list(label_map.keys())}")
        return label_map

    # --- vvvvvv MAJOR CHANGES IN THIS METHOD vvvvvv ---
    def execute_node(self, node):
        """The core dispatcher that executes a single AST node."""
        node_type = node.get('type')
        
        # We no longer just print, we process.
        # print(f"Executing node: {node_type}") 

        # In the Simulator.execute_node method...

        if node_type == 'variable_assignment':
            # NEW, SIMPLER, CORRECT LOGIC
            expression = node.get('expression', '')
            code_to_execute = expression.lstrip('$').strip()

            try:
                # Step 1: Execute the code directly on our game state dictionary.
                # This is what we had in Task 21. It correctly modifies the dictionary.
                exec(code_to_execute, self.game_state.variables)

                # Step 2: After execution, clean up the dictionary by removing the
                # built-ins that exec adds. This prevents the JSON error.
                if '__builtins__' in self.game_state.variables:
                    del self.game_state.variables['__builtins__']
                
                print(f"EXECUTED: {code_to_execute}")

            except Exception as e:
                print(f"ERROR executing expression '{code_to_execute}': {e}")

    def run_from_label(self, start_label_name):
        # --- NO CHANGES IN THIS METHOD ---
        if start_label_name not in self.labels:
            print(f"Error: Label '{start_label_name}' not found.")
            return

        print(f"\n--- Starting simulation from label '{start_label_name}' ---")
        start_node = self.labels[start_label_name]
        self.execute_node(start_node)
        print("--- Simulation finished ---")
        print("\nFinal Game State:")
        print(json.dumps(self.game_state.variables, indent=2))


def main():
    # --- NO CHANGES IN THIS FUNCTION ---
    try:
        with open('/content/output_v5.json', 'r') as f:
            ast = json.load(f)
    except FileNotFoundError:
        print("Error: AST file '/content/output_v5.json' not found.")
        print("Please run the parser first to generate it.")
        return

    sim = Simulator(ast)
    sim.run_from_label('start')

if __name__ == "__main__":
    main()