import sys
import json
import re

def parse_renpy_script(file_path):
    """
    Parses a simplified Ren'py script file and returns its AST as a dictionary.

    Args:
        file_path (str): The path to the .rpy file.

    Returns:
        dict: A dictionary representing the Abstract Syntax Tree of the script.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(json.dumps({"error": f"File not found: {file_path}"}, indent=2))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({"error": f"An error occurred: {e}"}, indent=2))
        sys.exit(1)

    root = {
        "ast_type": "root",
        "children": []
    }

    # parent_stack keeps track of (node, indentation_level)
    parent_stack = [(root, -1)]

    for line in lines:
        stripped_line = line.strip()

        # Ignore empty lines and comments
        if not stripped_line or stripped_line.startswith('#'):
            continue

        # Calculate indentation (count leading spaces)
        indentation = len(line) - len(line.lstrip(' '))

        # Adjust parent stack based on indentation
        while indentation <= parent_stack[-1][1]:
            parent_stack.pop()

        parent_node = parent_stack[-1][0]
        
        # Remove inline comments
        line_content = stripped_line.split('#')[0].strip()

        new_node = None

        # Determine node type and parse
        if line_content.startswith('label ') and line_content.endswith(':'):
            name = line_content[6:-1].strip()
            new_node = {
                "type": "label",
                "name": name,
                "children": []
            }
        elif line_content.startswith('if ') and line_content.endswith(':'):
            condition = line_content[3:-1].strip()
            new_node = {
                "type": "if_statement",
                "condition": condition,
                "children": []
            }
        elif line_content.startswith('$'):
            new_node = {
                "type": "variable_assignment",
                "expression": line_content
            }
        else:
            # Dialogue parsing: character "text"
            dialogue_match = re.match(r'(\w+)\s+"([^"]*)"$', line_content)
            if dialogue_match:
                character, text = dialogue_match.groups()
                new_node = {
                    "type": "dialogue",
                    "character": character,
                    "text": text
                }

        if new_node:
            parent_node.get("children", []).append(new_node)
            # If the new node can have children, push it to the stack
            if "children" in new_node:
                parent_stack.append((new_node, indentation))
    
    return root

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({
            "error": "Usage: python your_script_name.py <path_to_rpy_file>"
        }, indent=2))
        sys.exit(1)

    input_file_path = sys.argv[1]
    ast = parse_renpy_script(input_file_path)
    
    # Print the final JSON string to standard output
    print(json.dumps(ast, indent=2))
