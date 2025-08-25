import sys
import json
import re

def parse_rpy_to_ast(script_content):
    """
    Parses a simplified Ren'py script content into a JSON AST.

    The function processes the script line by line, using an indentation-based
    stack to manage the hierarchy of the AST. Each line is classified into a
    node type (e.g., label, command, dialogue, if_statement) and added to the
    tree.

    Args:
        script_content (str): The string content of the .rpy file.

    Returns:
        dict: A dictionary representing the root of the Abstract Syntax Tree.
    """
    root = {"ast_type": "root", "children": []}
    # The parent stack stores tuples of (indentation_level, node_object)
    parent_stack = [(-1, root)]

    lines = script_content.splitlines()

    for line in lines:
        stripped_line = line.strip()

        # Ignore empty lines and comments
        if not stripped_line or stripped_line.startswith('#'):
            continue

        indentation = len(line) - len(line.lstrip(' '))
        content = stripped_line

        # Adjust the parent stack based on the current line's indentation.
        # This handles "dedenting" and moving up the tree.
        while indentation <= parent_stack[-1][0]:
            parent_stack.pop()

        parent_node = parent_stack[-1][1]
        new_node = None
        is_block_starter = False # Flag for nodes that expect an indented block

        # --- Line Parsing Logic (order of checks is important) ---

        # Label: label <name>:
        if content.startswith('label ') and content.endswith(':'):
            name = content[6:-1].strip()
            new_node = {
                "type": "label",
                "name": name,
                "children": []
            }
            parent_node["children"].append(new_node)
            is_block_starter = True

        # Menu: menu:
        elif content == 'menu:':
            new_node = {
                "type": "menu",
                "children": []
            }
            parent_node["children"].append(new_node)
            is_block_starter = True

        # Choice: "<text>":
        elif content.startswith('"') and content.endswith('":'):
            text = content[1:-2]
            new_node = {
                "type": "choice",
                "text": text,
                "children": []
            }
            if parent_node.get("type") == "menu":
                parent_node["children"].append(new_node)
            is_block_starter = True

        # If statement: if <condition>:
        elif content.startswith('if ') and content.endswith(':'):
            condition = content[3:-1].strip()
            new_node = {
                "type": "if_statement",
                "condition": condition,
                "children": []
            }
            parent_node["children"].append(new_node)
            is_block_starter = True

        # Elif statement: elif <condition>:
        elif content.startswith('elif ') and content.endswith(':'):
            condition = content[5:-1].strip()
            new_node = {
                "type": "elif_statement",
                "condition": condition,
                "children": []
            }
            # Attach this to the preceding if_statement
            last_sibling = parent_node["children"][-1] if parent_node["children"] else None
            if last_sibling and last_sibling.get("type") == "if_statement":
                if "elif_blocks" not in last_sibling:
                    last_sibling["elif_blocks"] = []
                last_sibling["elif_blocks"].append(new_node)
            is_block_starter = True

        # Else statement: else:
        elif content == 'else:':
            new_node = {
                "type": "else_statement",
                "children": []
            }
            # Attach this to the preceding if_statement
            last_sibling = parent_node["children"][-1] if parent_node["children"] else None
            if last_sibling and last_sibling.get("type") == "if_statement":
                last_sibling["else_block"] = new_node
            is_block_starter = True

        # Variable Assignment: $ ...
        elif content.startswith('$'):
            new_node = {
                "type": "variable_assignment",
                "expression": content
            }
            parent_node["children"].append(new_node)

        # Dialogue: <character> "<text>"
        elif (match := re.match(r'^(\w+)\s+"(.*)"$', content)):
            character, text = match.groups()
            new_node = {
                "type": "dialogue",
                "character": character,
                "text": text
            }
            parent_node["children"].append(new_node)

        # Command (fallback for simple keywords)
        else:
            parts = content.split(' ', 1)
            keyword = parts[0]
            args = parts[1] if len(parts) > 1 else ""
            new_node = {
                "type": "command",
                "keyword": keyword,
                "args": args
            }
            parent_node["children"].append(new_node)

        # If the new node starts a block, push it to the stack to become
        # the new parent for subsequent indented lines.
        if is_block_starter and new_node:
            parent_stack.append((indentation, new_node))

    return root


def main():
    """
    Main function to run the script from the command line.
    It reads the input file, calls the parser, and prints the resulting JSON.
    """
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "<path_to_rpy_file>", file=sys.stderr)
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{input_file_path}'", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    ast = parse_rpy_to_ast(script_content)

    # Print the final JSON to standard output with specified formatting
    print(json.dumps(ast, indent=2))


if __name__ == "__main__":
    main()