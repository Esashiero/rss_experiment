import json

class GameState:
    """A class to hold the state of the game's variables."""
    def __init__(self):
        # All Ren'py variables will be stored here.
        self.variables = {}
        print("GameState initialized.")

    def set_variable(self, name, value):
        """Sets or updates a variable."""
        # Note: In Ren'py, variable names don't include the $.
        clean_name = name.strip().lstrip('$').strip()
        self.variables[clean_name] = value
        print(f"STATE_UPDATE: {clean_name} = {value}")

    def get_variable(self, name):
        """Retrieves a variable's value."""
        clean_name = name.strip().lstrip('$').strip()
        return self.variables.get(clean_name)

class Simulator:
    """
    The main engine that traverses the AST and simulates the game's state.
    """
    def __init__(self, ast):
        self.ast = ast
        self.game_state = GameState()
        # A map to quickly find labels in the AST.
        self.labels = self._find_all_labels()
        print("Simulator initialized.")

    def _find_all_labels(self):
        """Pre-processes the AST to find all label nodes for quick access."""
        label_map = {}
        for node in self.ast['children']:
            if node['type'] == 'label':
                label_map[node['name']] = node
        print(f"Found labels: {list(label_map.keys())}")
        return label_map

    def execute_node(self, node):
        """The core dispatcher that executes a single AST node."""
        node_type = node.get('type')

        # This will be the brain of our simulator.
        # For now, we just print the type of node we encounter.
        print(f"Executing node: {node_type}")

        if node_type == 'variable_assignment':
            # TODO: Implement the logic to parse and set variables.
            pass
        elif node_type == 'if_statement':
            # TODO: Implement the logic to evaluate the condition and branch.
            pass
        elif node_type in ['label', 'choice', 'menu', 'elif_statement', 'else_statement']:
            # For container nodes, we just execute their children.
            for child_node in node.get('children', []):
                self.execute_node(child_node)
        # Other nodes like 'command' and 'dialogue' can be ignored for now.


    def run_from_label(self, start_label_name):
        """Starts the simulation from a specific label."""
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
    """
    A simple main function to test the simulator.
    It loads the AST from a file and runs the simulation.
    """
    try:
        with open('/content/output_v5.json', 'r') as f:
            ast = json.load(f)
    except FileNotFoundError:
        print("Error: AST file '/content/output_v5.json' not found.")
        print("Please run the parser first to generate it.")
        return

    # Create the simulator and run it
    sim = Simulator(ast)
    sim.run_from_label('start')

if __name__ == "__main__":
    main()