import json
import operator

class GameState:
    """A class to hold the state of the game's variables."""
    def __init__(self):
        self.variables = {}

    def __str__(self):
        # For pretty printing the final state
        return json.dumps(self.variables, indent=2)

class Simulator:
    """
    The main engine that traverses the AST and simulates the game's state.
    This version parses expressions manually for stability.
    """
    def __init__(self, ast):
        self.ast = ast
        self.game_state = GameState()
        self.labels = self._find_all_labels()
        # A map of operators to their functions (e.g., "+=" -> operator.iadd)
        self.operators = {
            "=": operator.setitem,
            "+=": operator.iadd,
            "-=": operator.isub
        }
        print("Simulator (V2) initialized.")

    def _find_all_labels(self):
        """Pre-processes the AST to find all label nodes for quick access."""
        label_map = {}
        for node in self.ast['children']:
            if node['type'] == 'label':
                label_map[node['name']] = node
        print(f"Found labels: {list(label_map.keys())}")
        return label_map

    def _evaluate_value(self, value_str):
        """
        Converts a string value from the script into a Python object.
        E.g., "100" -> 100, "\"Alex\"" -> "Alex", "True" -> True
        """
        value_str = value_str.strip()
        # Boolean
        if value_str == 'True':
            return True
        if value_str == 'False':
            return False
        # String
        if value_str.startswith('"') and value_str.endswith('"'):
            return value_str[1:-1]
        # Integer
        try:
            return int(value_str)
        except ValueError:
            pass
        # Float
        try:
            return float(value_str)
        except ValueError:
            pass
        # Fallback: could be a variable name
        return self.game_state.variables.get(value_str, None)

    def _execute_variable_assignment(self, node):
        """
        Manually parses and executes a variable assignment expression.
        Example: "$ score -= 25"
        """
        expression = node.get('expression', '').lstrip('$').strip()
        
        # Find which operator is being used
        op_key = None
        for op in self.operators:
            if op in expression:
                op_key = op
                break

        if not op_key:
            print(f"Warning: Could not parse expression: {expression}")
            return
            
        parts = [p.strip() for p in expression.split(op_key, 1)]
        variable_name = parts[0]
        value_str = parts[1]

        # Convert the string value to a real type (int, string, bool, etc.)
        value = self._evaluate_value(value_str)

        print(f"EXECUTED: {variable_name} {op_key} {value}")

        # Apply the operation
        if op_key == "=":
            self.game_state.variables[variable_name] = value
        elif op_key in ["+=", "-="]:
            # For += and -=, we need to ensure the variable exists first
            if variable_name not in self.game_state.variables:
                self.game_state.variables[variable_name] = 0 # Default to 0
            
            op_func = self.operators[op_key]
            # Perform the operation in-place
            self.game_state.variables[variable_name] = op_func(self.game_state.variables[variable_name], value)

    def execute_node(self, node):
        """The core dispatcher that executes a single AST node."""
        node_type = node.get('type')

        if node_type == 'variable_assignment':
            self._execute_variable_assignment(node)
        
        # For container nodes, recursively execute their children
        if 'children' in node:
            for child_node in node.get('children', []):
                self.execute_node(child_node)

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
        print(self.game_state)


def main():
    """Main function to test the simulator."""
    try:
        with open('/content/output_v5.json', 'r') as f:
            ast = json.load(f)
    except FileNotFoundError:
        print("Error: AST file '/content/output_v5.json' not found.")
        return

    sim = Simulator(ast)
    sim.run_from_label('start')

if __name__ == "__main__":
    main()