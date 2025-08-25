import json
import operator

class GameState:
    """A class to hold the state of the game's variables."""
    def __init__(self):
        self.variables = {}

    def __str__(self):
        return json.dumps(self.variables, indent=2)

class Simulator:
    """
    The main engine that traverses the AST and simulates the game's state.
    """
    def __init__(self, ast):
        self.ast = ast
        self.game_state = GameState()
        self.labels = self._find_all_labels()
        self.operators = {
            "=": operator.setitem, "+=": operator.iadd, "-=": operator.isub
        }
        # A map for boolean comparisons
        self.comparisons = {
            ">": operator.gt, "<": operator.lt, "==": operator.eq, "!=": operator.ne,
            ">=": operator.ge, "<=": operator.le
        }
        print("Simulator (V3) initialized.")

    def _find_all_labels(self):
        label_map = {}
        for node in self.ast['children']:
            if node['type'] == 'label':
                label_map[node['name']] = node
        print(f"Found labels: {list(label_map.keys())}")
        return label_map

    def _evaluate_value(self, value_str):
        value_str = value_str.strip()
        if value_str == 'True': return True
        if value_str == 'False': return False
        if value_str.startswith('"') and value_str.endswith('"'): return value_str[1:-1]
        try: return int(value_str)
        except ValueError: pass
        try: return float(value_str)
        except ValueError: pass
        return self.game_state.variables.get(value_str, None)

    def _evaluate_condition(self, condition_str):
        """
        Parses and evaluates a simple boolean condition.
        Example: "score > 80" or "player_name == \"Alex\""
        """
        for op_key, op_func in self.comparisons.items():
            if op_key in condition_str:
                parts = [p.strip() for p in condition_str.split(op_key, 1)]
                left_val_str, right_val_str = parts[0], parts[1]
                
                left_val = self._evaluate_value(left_val_str)
                right_val = self._evaluate_value(right_val_str)

                if left_val is None: return False # Variable not found
                
                result = op_func(left_val, right_val)
                print(f"EVALUATED: ({left_val} {op_key} {right_val}) -> {result}")
                return result
        print(f"Warning: Could not evaluate condition: {condition_str}")
        return False

    def _execute_variable_assignment(self, node):
        expression = node.get('expression', '').lstrip('$').strip()
        op_key = None
        for op in self.operators:
            if op in expression: op_key = op; break
        if not op_key: return

        parts = [p.strip() for p in expression.split(op_key, 1)]
        variable_name, value_str = parts[0], parts[1]
        value = self._evaluate_value(value_str)
        print(f"EXECUTED: {variable_name} {op_key} {value}")

        if op_key == "=": self.game_state.variables[variable_name] = value
        elif op_key in ["+=", "-="]:
            if variable_name not in self.game_state.variables: self.game_state.variables[variable_name] = 0
            op_func = self.operators[op_key]
            self.game_state.variables[variable_name] = op_func(self.game_state.variables[variable_name], value)

    def _execute_if_statement(self, node):
        """Executes a full if/elif/else chain."""
        # Check the main 'if' condition
        if_condition = node.get('condition', 'False')
        if self._evaluate_condition(if_condition):
            for child_node in node.get('children', []):
                self.execute_node(child_node)
            return # Exit after executing a true block

        # Check 'elif' blocks if they exist
        for elif_block in node.get('elif_blocks', []):
            elif_condition = elif_block.get('condition', 'False')
            if self._evaluate_condition(elif_condition):
                for child_node in elif_block.get('children', []):
                    self.execute_node(child_node)
                return # Exit after executing a true block
        
        # Execute 'else' block if it exists and no other block was executed
        if 'else_block' in node:
            for child_node in node['else_block'].get('children', []):
                self.execute_node(child_node)

    def execute_node(self, node):
        """The core dispatcher that executes a single AST node."""
        node_type = node.get('type')

        if node_type == 'variable_assignment':
            self._execute_variable_assignment(node)
        elif node_type == 'if_statement':
            self._execute_if_statement(node)
        
        # For simple container nodes, recursively execute their children
        elif 'children' in node and node_type not in ['if_statement']:
             for child_node in node.get('children', []):
                self.execute_node(child_node)

    def run_simulation(self, start_label_name):
        """Starts the simulation from a specific label."""
        if start_label_name not in self.labels:
            print(f"Error: Label '{start_label_name}' not found.")
            return

        print(f"\n--- Starting simulation from label '{start_label_name}' ---")
        # First, run the 'start' label to initialize variables.
        # This is a simplification; a real game could start anywhere.
        if start_label_name != 'start':
            print("Initializing state from 'start' label...")
            start_node = self.labels['start']
            self.execute_node(start_node)
            print("Initialization complete.")

        # Now, run the target label
        target_node = self.labels[start_label_name]
        if start_label_name == 'start': # Avoid running 'start' twice
            # Re-fet