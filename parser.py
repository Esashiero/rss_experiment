#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re
import os

def _extract_character_map(combined_content):
    """
    Scans the script content for character definitions and creates a mapping.
    e.g., 'define a = Character("Ami", ...)' -> {"a": "Ami"}
    """
    char_map = {}
    # Regex to find character definitions
    char_regex = re.compile(r'define\s+([a-zA-Z0-9_]+)\s*=\s*Character\s*\(\s*"([^"]+)"')
    
    for line in combined_content.splitlines():
        match = char_regex.search(line)
        if match:
            var, name = match.groups()
            char_map[var] = name
            print(f"Found character: {var} -> {name}", file=sys.stderr)
            
    return char_map

def parse_rpy_to_ast(script_content):
    """Parses a combined string of all game scripts into a single AST."""
    
    # First, build the character map from the entire script
    character_map = _extract_character_map(script_content)

    root = {"ast_type": "root", "children": []}
    parent_stack = [(-1, root)]
    lines = script_content.splitlines()

    KNOWN_COMMANDS = ["scene", "show", "hide", "play", "stop", "jump", "return", "call", "snapshot"]
    
    skipping_block = False
    skip_indent = -1

    for line in lines:
        stripped_line = line.strip()

        if skipping_block: # Handles skipping python blocks
            if not stripped_line: continue
            current_indent = len(line) - len(line.lstrip(' '))
            if current_indent > skip_indent: continue
            else: skipping_block = False

        content = stripped_line.split('#', 1)[0].strip()
        if not content: continue

        indentation = len(line) - len(line.lstrip(' '))

        if content.endswith("python:"):
            skipping_block = True
            skip_indent = indentation
            continue

        while indentation <= parent_stack[-1][0]:
            parent_stack.pop()

        parent_node = parent_stack[-1][1]
        new_node = None
        is_block_starter = False
        
        keyword = content.split(' ', 1)[0]

        if keyword == "with":
            # Attach transition to the last node
            if parent_node["children"]:
                parent_node["children"][-1]["transition"] = content.split(' ', 1)[1] if ' ' in content else ""
            continue
        
        if keyword == "init" or (keyword.startswith("init") and content.endswith(":")):
            priority_match = re.search(r'init\s+(-?\d+)', content)
            priority = int(priority_match.group(1)) if priority_match else 0
            new_node = {"type": "init_block", "priority": priority, "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif keyword in KNOWN_COMMANDS:
            args = content.split(' ', 1)[1] if ' ' in content else ""
            new_node = {"type": "command", "keyword": keyword, "args": args}
            parent_node["children"].append(new_node)
        elif content.startswith('label ') and content.endswith(':'):
            name = content[6:-1].strip()
            new_node = {"type": "label", "name": name, "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content.startswith('menu') and content.endswith(':'):
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
        # Simplified elif/else handling, assuming they are direct children for parsing
        elif content.startswith('elif ') and content.endswith(':'):
            condition = content[5:-1].strip()
            new_node = {"type": "elif_statement", "condition": condition, "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content == 'else:':
            new_node = {"type": "else_statement", "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content.startswith('$'):
            new_node = {"type": "variable_assignment", "expression": content}
            parent_node["children"].append(new_node)
        elif (match := re.match(r'^([\w."]+)\s+"(.*)"$', content)):
            char_var, text = match.groups()
            # --- CHARACTER NAME RESOLUTION ---
            # Use the character_map to get the full name
            character_name = character_map.get(char_var, char_var)
            new_node = {"type": "dialogue", "character": character_name, "text": text}
            parent_node["children"].append(new_node)
        elif content.startswith('"') and content.endswith('"'):
            text = content[1:-1]
            new_node = {"type": "dialogue", "character": "narrator", "text": text}
            parent_node["children"].append(new_node)
        else:
            if not content.startswith(('define', 'image')):
                pass # Silently ignore unrecognized lines like definitions

        if is_block_starter and new_node:
            parent_stack.append((indentation, new_node))

    return root

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <path_to_game_directory>", file=sys.stderr)
        sys.exit(1)
        
    game_directory = sys.argv[1]
    if not os.path.isdir(game_directory):
        print(f"Error: Path '{game_directory}' is not a valid directory.", file=sys.stderr)
        sys.exit(1)

    combined_script_content = ""
    print("--- Reading all .rpy files from directory ---", file=sys.stderr)
    for root, _, files in os.walk(game_directory):
        for file in files:
            if file.endswith(".rpy"):
                file_path = os.path.join(root, file)
                print(f"Reading: {file_path}", file=sys.stderr)
                try:
                    with open(file_path, 'r', encoding='utf-8-sig') as f:
                        combined_script_content += f.read() + "\n"
                except Exception as e:
                    print(f"Warning: Could not read file {file_path}. Error: {e}", file=sys.stderr)

    if not combined_script_content:
        print("Error: No .rpy files found or read from the directory.", file=sys.stderr)
        sys.exit(1)

    ast = parse_rpy_to_ast(combined_script_content)
    print(json.dumps(ast, indent=2))

if __name__ == "__main__":
    main()