import json
import sys
import re

def get_indentation(line):
    """Calculates the indentation level of a line."""
    return len(line) - len(line.lstrip(' '))

def parse_renpy_script(file_content):
    """
    Parses a simplified Ren'py script and builds an Abstract Syntax Tree (AST).
    """
    root = {
        "ast_type": "root",
        "children": []
    }

    # Stack to keep track of the current parent node and its indentation level
    # Each element is a tuple: (node, indentation_level)
    stack = [(root, -1)]
    
    lines = file_content.split('\n')

    for line in lines:
        stripped_line = line.strip()

        # Ignore empty lines and comments
        if not stripped_line or stripped_line.startswith('#'):
            continue

        indentation = get_indentation(line)

        # Adjust the stack based on the current indentation level
        while indentation <= stack[-1][1]:
            stack.pop()
        
        parent_node = stack[-1][0]
        
        new_node = None

        # Statement parsing
        if stripped_line.startswith('label'):
            match = re.match(r'label\s+(.+?):', stripped_line)
            if match:
                new_node = {
                    "type": "label",
                    "name": match.group(1),
                    "children": []
                }
        elif stripped_line.startswith('$'):
            new_node = {
                "type": "variable_assignment",
                "expression": stripped_line
            }
        elif stripped_line.startswith('if'):
            new_node = {
                "type": "if_statement",
                "condition": stripped_line.rstrip(':'),
                "children": []
            }
        elif stripped_line.startswith('menu:'):
            new_node = {
                "type": "menu",
                "children": []
            }
        elif stripped_line.startswith('"') and stripped_line.endswith('":'):
            if parent_node.get("type") == "menu":
                choice_text = stripped_line[1:-2]
                new_node = {
                    "type": "choice",
                    "text": choice_text,
                    "children": []
                }
        else:
            # Dialogue
            match = re.match(r'(\w+)\s+"(.+)"', stripped_line)
            if match:
                new_node = {
                    "type": "dialogue",
                    "character": match.group(1),
                    "text": match.group(2)
                }

        if new_node:
            if "children" not in parent_node:
                parent_node["children"] = []
            parent_node["children"].append(new_node)
            
            # If the new node is a block statement, push it onto the stack
            if "children" in new_node:
                stack.append((new_node, indentation))

    return root

def main():
    """
    Main function to handle file input and JSON output.
    """
    if len(sys.argv) != 2:
        print("Usage: python llm_parser_v2.py <input_file.rpy>", file=sys.stderr)
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{input_file_path}'", file=sys.stderr)
        sys.exit(1)

    ast = parse_renpy_script(file_content)
    
    # Print the final JSON output
    print(json.dumps(ast, indent=2))

if __name__ == "__main__":
    main()