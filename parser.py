# parser.py (V6 - The Multi-Line Aware, Final Parser)
import sys
import json
import re
import os

KNOWN_COMMANDS = {"scene", "show", "hide", "play", "stop", "jump", "return", "call", "snapshot"}

def _extract_character_map(content):
    char_map = {}
    char_regex = re.compile(r'define\s+([a-zA-Z0-9_]+)\s*=\s*Character\s*\(\s*"([^"]+)"')
    for match in char_regex.finditer(content):
        var, name = match.groups()
        char_map[var] = name
    return char_map

def parse_rpy_to_ast(script_content):
    character_map = _extract_character_map(script_content)
    root = {"ast_type": "root", "children": []}
    parent_stack = [(-1, root)]
    
    # Pre-process to handle multi-line statements by joining them
    # This is a more robust approach than a complex state machine
    processed_lines = []
    line_buffer = ""
    for line in script_content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue # Skip empty lines and comments
        
        line_buffer += " " + stripped
        if line_buffer.count('(') == line_buffer.count(')') and line_buffer.strip().endswith(':'):
            # The statement is complete (balanced parentheses and ends with a colon)
            processed_lines.append(line) # Use the original line with indentation
            line_buffer = ""
        elif not (stripped.startswith('if ') or stripped.startswith('elif ')):
             # It's not the start of a multi-line if, so treat as a single line
             processed_lines.append(line)
             line_buffer = ""
             
    # Fallback for any dangling buffer content
    if line_buffer.strip():
        processed_lines.append(line_buffer)

    lines = script_content.splitlines() # We still need original lines for indentation
    
    # This is a simplification. A truly robust multi-line parser is much more complex.
    # We will combine lines that are part of a multi-line `if` condition.
    
    temp_lines = []
    in_multiline_if = False
    buffer = ''
    
    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith('if ') and not stripped.endswith(':'):
            in_multiline_if = True
            buffer = line
            continue
            
        if in_multiline_if:
            buffer += ' ' + stripped
            if stripped.endswith(':'):
                in_multiline_if = False
                temp_lines.append(buffer)
                buffer = ''
            continue
            
        temp_lines.append(line)
    lines = temp_lines

    for line in lines:
        stripped_line = line.lstrip()
        indentation = len(line) - len(stripped_line)
        content = stripped_line.split('#', 1)[0].strip()

        if not content or content.startswith('python:'):
            continue

        while indentation <= parent_stack[-1][0]:
            parent_stack.pop()
        parent_node = parent_stack[-1][1]

        new_node, is_block_starter = None, False
        
        # This logic should now receive the combined multi-line if statement
        if content.startswith('if ') and content.endswith(':'):
            condition = content[3:-1].replace('\n', ' ').strip()
            new_node = {"type": "if_statement", "condition": condition, "children": []}
            is_block_starter = True
        elif content.startswith('elif ') and content.endswith(':'):
            condition = content[5:-1].strip()
            new_node = {"type": "elif_statement", "condition": condition, "children": []}
            is_block_starter = True
        elif content.startswith('label ') and content.endswith(':'):
            name = content[6:-1].strip()
            new_node = {"type": "label", "name": name, "children": []}
            is_block_starter = True
        elif content.startswith('menu'):
            new_node = {"type": "menu", "children": []}
            is_block_starter = True
        # ... (rest of the logic from V5 is mostly fine) ...
        elif content == 'else:':
            new_node = {"type": "else_statement", "children": []}
            is_block_starter = True
        elif content.startswith('"') and content.endswith(':'):
            full_choice_text = content[1:-2]
            text, condition = (full_choice_text.rsplit(" if ", 1) + [None])[:2]
            new_node = {"type": "choice", "text": text, "children": []}
            if condition: new_node["condition"] = condition
            is_block_starter = True
        else:
            keyword = content.split(' ', 1)[0]
            if keyword in KNOWN_COMMANDS:
                args = content.split(' ', 1)[1] if ' ' in content else ""
                new_node = {"type": "command", "keyword": keyword, "args": args}
            elif content.startswith('$'):
                new_node = {"type": "variable_assignment", "expression": content}
            elif (match := re.match(r'^([\w."]+)\s+"(.*)"$', content)):
                char_var, text = match.groups()
                new_node = {"type": "dialogue", "character": character_map.get(char_var, char_var), "text": text}
            elif content.startswith('"') and content.endswith('"'):
                new_node = {"type": "dialogue", "character": "narrator", "text": content[1:-1]}
        
        if new_node:
            parent_node["children"].append(new_node)
            if is_block_starter:
                parent_stack.append((indentation, new_node))

    return root

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <game_directory>", file=sys.stderr); sys.exit(1)
    game_dir = sys.argv[1]
    if not os.path.isdir(game_dir):
        print(f"Error: Path '{game_dir}' is not a valid directory.", file=sys.stderr); sys.exit(1)
    
    content = ""
    for root, _, files in os.walk(game_dir):
        for file in sorted(files):
            if file.endswith(".rpy"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                        content += f.read() + "\n"
                except Exception as e:
                    print(f"Warning: Could not read {path}. Error: {e}", file=sys.stderr)
    
    ast = parse_rpy_to_ast(content)
    print(json.dumps(ast, indent=2))

if __name__ == "__main__":
    main()