import json
import operator

class GameState:
    def __init__(self):
        self.variables = {}
    def __str__(self):
        return json.dumps(self.variables, indent=2)

class Simulator:
    def __init__(self, ast):
        self.ast = ast
        self.game_state = GameState()
        self.labels = self._find_all_labels()
        self.operators = {"=": operator.setitem, "+=": operator.iadd, "-=": operator.isub}
        self.comparisons = {">": operator.gt, "<": operator.lt, "==": operator.eq, "!=": operator.ne, ">=": operator.ge, "<=": operator.le}
        print("Simulator (V4) initialized.")

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
        for op_key, op_func in self.comparisons.items():
            if op_key in condition_str:
                parts = [p.strip() for p in condition_str.split(op_key, 1)]
                left_val = self._evaluate_value(parts[0])
                right_val = self._evaluate_value(parts[1])
                if left_val is None: return False
                result = op_func(left_val, right_val)
                print(f"EVALUATED: ({parts[0]} {op_key} {parts[1]}) -> {result}")
                return result
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
        if self._evaluate_condition(node.get('condition', 'False')):
            for child_node in node.get('children', []): self.execute_node(child_node)
            return
        for elif_block in node.get('elif_blocks', []):
            if self._evaluate_condition(elif_block.get('condition', 'False')):
                for child_node in elif_block.get('children', []): self.execute_node(child_node)
                return
        if 'else_block' in node:
            for child_node in node['else_block'].get('children', []): self.execute_node(child_node)

    def take_snapshot(self, filename):
        print(f"--- Taking snapshot: {filename} ---")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(str(self.game_state))
        print("Snapshot saved successfully.")

    def execute_node(self, node):
        node_type = node.get('type')
        if node_type == 'variable_assignment': self._execute_variable_assignment(node)
        elif node_type == 'if_statement': self._execute_if_statement(node)
        elif node_type == 'command' and node.get('keyword') == 'snapshot':
            self.take_snapshot(node.get('args'))
        elif 'children' in node and node_type not in ['if_statement']:
             for child_node in node.get('children', []): self.execute_node(child_node)

    def run_from_label(self, start_label_name):
        if start_label_name not in self.labels: return
        print(f"\n--- Starting simulation from label '{start_label_name}' ---")
        self.execute_node(self.labels[start_label_name])
        print("--- Simulation finished ---")
        print("\nFinal State for this run:")
        print(self.game_state)

def main():
    ast_file = '/content/output_v5.json'
    parser_script = 'llm_parser_v5.py'
    sample_file = 'sample_v1.rpy'
    
    # We now run the parser using a subprocess to be clean.
    import subprocess
    print(f"--- Generating AST from {sample_file} ---")
    with open(ast_file, 'w') as f:
        subprocess.run(['python', parser_script, sample_file], stdout=f, text=True)
    print(f"AST file generated at {ast_file}")

    try:
        with open(ast_file, 'r') as f:
            ast = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error: Could not load AST file.")
        return

    sim = Simulator(ast)
    sim.run_from_label('start')
    sim.run_from_label('test_logic')

if __name__ == "__main__":
    main()