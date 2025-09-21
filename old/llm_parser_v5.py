#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re

def parse_rpy_to_ast(script_content):
    root = {"ast_type": "root", "children": []}
    parent_stack = [(-1, root)]
    lines = script_content.splitlines()

    # Define a list of known command keywords for robust checking
    KNOWN_COMMANDS = ["scene", "show", "hide", "play", "stop", "jump", "return", "snapshot"]

    for line in lines:
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith('#'):
            continue

        indentation = len(line) - len(line.lstrip(' '))
        content = stripped_line

        while indentation <= parent_stack[-1][0]:
            parent_stack.pop()

        parent_node = parent_stack[-1][1]
        new_node = None
        is_block_starter = False

        # --- Use a more robust check for commands first ---
        parts = content.split(' ', 1)
        keyword = parts[0]

        if keyword in KNOWN_COMMANDS:
            args = parts[1] if len(parts) > 1 else ""
            new_node = {"type": "command", "keyword": keyword, "args": args}
            parent_node["children"].append(new_node)
        elif content.startswith('label ') and content.endswith(':'):
            name = content[6:-1].strip()
            new_node = {"type": "label", "name": name, "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content == 'menu:':
            new_node = {"type": "menu", "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content.startswith('"') and content.endswith('":'):
            text = content[1:-2]
            new_node = {"type": "choice", "text": text, "children": []}
            if parent_node.get("type") == "menu":
                parent_node["children"].append(new_node)
            is_block_starter = True
        elif content.startswith('if ') and content.endswith(':'):
            condition = content[3:-1].strip()
            new_node = {"type": "if_statement", "condition": condition, "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content.startswith('elif ') and content.endswith(':'):
            condition = content[5:-1].strip()
            new_node = {"type": "elif_statement", "condition": condition, "children": []}
            last_sibling = parent_node["children"][-1] if parent_node["children"] else None
            if last_sibling and last_sibling.get("type") == "if_statement":
                if "elif_blocks" not in last_sibling:
                    last_sibling["elif_blocks"] = []
                last_sibling["elif_blocks"].append(new_node)
            is_block_starter = True
        elif content == 'else:':
            new_node = {"type": "else_statement", "children": []}
            last_sibling = parent_node["children"][-1] if parent_node["children"] else None
            if last_sibling and last_sibling.get("type") == "if_statement":
                last_sibling["else_block"] = new_node
            is_block_starter = True
        elif content.startswith('$'):
            new_node = {"type": "variable_assignment", "expression": content}
            parent_node["children"].append(new_node)
        elif (match := re.match(r'^(\w+)\s+"(.*)"$', content)):
            character, text = match.groups()
            new_node = {"type": "dialogue", "character": character, "text": text}
            parent_node["children"].append(new_node)
        else:
            print(f"Warning: Unrecognized line format: {content}", file=sys.stderr)

        if is_block_starter and new_node:
            parent_stack.append((indentation, new_node))

    return root

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_rpy_file>", file=sys.stderr)
        sys.exit(1)
    input_file_path = sys.argv[1]
    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{input_file_path}'", file=sys.stderr)
        sys.exit(1)
    
    ast = parse_rpy_to_ast(script_content)
    print(json.dumps(ast, indent=2))

if __name__ == "__main__":
    main()