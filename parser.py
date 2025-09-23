#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re
import os

def _extract_character_map(combined_content):
    """Scans for character definitions and creates a mapping."""
    char_map = {}
    char_regex = re.compile(r'define\s+([a-zA-Z0-9_]+)\s*=\s*Character\s*\(\s*"([^"]+)"')
    
    for line in combined_content.splitlines():
        match = char_regex.search(line)
        if match:
            var, name = match.groups()
            char_map[var] = name
    return char_map

def parse_rpy_to_ast(script_content):
    """Parses a combined string of all game scripts into a single AST."""
    character_map = _extract_character_map(script_content)
    root = {"ast_type": "root", "children": []}
    parent_stack = [(-1, root)]
    lines = script_content.splitlines()
    KNOWN_COMMANDS = ["scene", "show", "hide", "play", "stop", "jump", "return", "call", "snapshot"]
    skipping_block = False
    skip_indent = -1

    for line in lines:
        stripped_line = line.strip()
        if skipping_block:
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

        while indentation <= parent_stack[-1][0]: parent_stack.pop()
        parent_node = parent_stack[-1][1]
        new_node, is_block_starter = None, False
        keyword = content.split(' ', 1)[0]

        if keyword == "with":
            if parent_node["children"]: parent_node["children"][-1]["transition"] = content.split(' ', 1)[1] if ' ' in content else ""
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
        elif content.startswith('menu'): # Handles menus with or without names
            new_node = {"type": "menu", "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        
        # --- PARSER UPGRADE FOR CONDITIONAL CHOICES ---
        elif content.startswith('"') and content.endswith(':'):
            full_choice_text = content[1:-2]
            text, condition = full_choice_text, None
            if " if " in full_choice_text:
                parts = full_choice_text.split(" if ", 1)
                text = parts[0]
                condition = parts[1]

            new_node = {"type": "choice", "text": text, "children": []}
            if condition:
                new_node["condition"] = condition
            
            if parent_node.get("type") == "menu": parent_node["children"].append(new_node)
            is_block_starter = True
        # --- END OF UPGRADE ---

        elif content.startswith('if ') and content.endswith(':'):
            condition = content[3:-1].strip()
            new_node = {"type": "if_statement", "condition": condition, "children": []}
            parent_node["children"].append(new_node)
            is_block_starter = True
        elif content.startswith('$'):
            new_node = {"type": "variable_assignment", "expression": content}
            parent_node["children"].append(new_node)
        elif (match := re.match(r'^([\w."]+)\s+"(.*)"$', content)):
            char_var, text = match.groups()
            character_name = character_map.get(char_var, char_var)
            new_node = {"type": "dialogue", "character": character_name, "text": text}
            parent_node["children"].append(new_node)
        elif content.startswith('"') and content.endswith('"'):
            text = content[1:-1]
            new_node = {"type": "dialogue", "character": "narrator", "text": text}
            parent_node["children"].append(new_node)

        if is_block_starter and new_node: parent_stack.append((indentation, new_node))

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
    for root, _, files in os.walk(game_directory):
        for file in sorted(files): # Sort for consistent order
            if file.endswith(".rpy"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8-sig') as f:
                        combined_script_content += f.read() + "\n"
                except Exception as e:
                    print(f"Warning: Could not read file {file_path}. Error: {e}", file=sys.stderr)

    ast = parse_rpy_to_ast(combined_script_content)
    print(json.dumps(ast, indent=2))

if __name__ == "__main__":
    main()