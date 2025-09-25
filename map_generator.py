# map_generator.py (V13 - The Definitive, Correctly Structured Version)
import json
import argparse
import sys
from collections import OrderedDict

# (All helper functions like _flatten_ast, recursive finders, etc., are unchanged and correct)
def _flatten_ast(hierarchical_ast):
    flat_ast = OrderedDict()
    for node in hierarchical_ast.get('children', []):
        if node.get('type') == 'label':
            label_name, children = node.get('name'), node.get('children', [])
            if label_name: flat_ast[label_name] = children
    return flat_ast

def _find_first_jump_recursively(node_list):
    for node in node_list:
        if node.get('type') == 'command' and node.get('keyword') == 'jump': return node.get('args')
        if 'children' in node:
            found_jump = _find_first_jump_recursively(node.get('children', []));
            if found_jump: return found_jump
    return None

def _extract_choices_recursively(menu_node):
    terminal_choices = OrderedDict()
    def _traverse(node_list, text_path, condition_path):
        current_menu = next((n for n in node_list if n.get('type') == 'menu'), None)
        if not current_menu:
            jump_target = _find_first_jump_recursively(node_list)
            if jump_target and text_path:
                 full_choice_text = " -> ".join(text_path)
                 terminal_choices[full_choice_text] = {"target": jump_target, "conditions": condition_path if condition_path else ["True"]}
            return
        for choice in current_menu.get('children', []):
            if choice.get('type') != 'choice': continue
            new_text_path = text_path + [choice.get('text')]
            new_condition_path = condition_path + ([choice.get('condition')] if choice.get('condition') else [])
            _traverse(choice.get('children', []), new_text_path, new_condition_path)
    _traverse([menu_node], [], [])
    return terminal_choices

def analyze_rpy_ast(hierarchical_ast):
    hubs, transitions, dispatchers = OrderedDict(), OrderedDict(), OrderedDict()
    global_ast = _flatten_ast(hierarchical_ast)
    all_labels = list(global_ast.keys())

    for i, (label_name, nodes) in enumerate(global_ast.items()):
        if not nodes: continue

        # --- THE DEFINITIVE, RESTRUCTURED LOGIC ---
        
        # 1. First, find the menu node, if one exists anywhere in the label.
        def find_menu_recursively(node_list):
            for node in node_list:
                if node.get('type') == 'menu': return node
                if 'children' in node:
                    found = find_menu_recursively(node.get('children', []));
                    if found: return found
            return None
        menu_node = find_menu_recursively(nodes)

        # 2. Parse ALL conditional jumps in the entire label.
        # This will find both pre-menu dispatchers and regular dispatchers.
        conditional_paths = []
        cond_nodes = [n for n in nodes if n.get('type') in ('if_statement', 'elif_statement', 'else_statement')]
        for node in cond_nodes:
            condition = "else" if node.get('type') == 'else_statement' else node.get('condition')
            if condition:
                jump_target = _find_first_jump_recursively(node.get('children', []))
                if jump_target: conditional_paths.append({"condition": condition, "target": jump_target})

        # 3. Now, classify the label based on what we found.
        if menu_node:
            choices = _extract_choices_recursively(menu_node)
            if len(choices) > 1:
                # It's a Hub. It gets the choices AND any conditional paths we found.
                hubs[label_name] = {"choices": choices, "conditional_paths": conditional_paths}
                continue
            elif len(choices) == 1:
                # A single-choice menu is just a transition.
                transitions[label_name] = list(choices.values())[0]["target"]
                continue
        
        # 4. If it's not a hub, it might be a pure dispatcher.
        if conditional_paths and not menu_node:
            dispatchers[label_name] = conditional_paths
            # Check for dispatcher fall-through
            if i < len(all_labels) - 1 and not any(p['condition'] == 'else' for p in conditional_paths):
                 if not any(c.get('type') == 'command' and c.get('keyword') == 'jump' for c in cond_nodes[-1].get('children', [])):
                    conditional_paths.append({"condition": "else", "target": all_labels[i + 1]})
            continue

        # 5. If nothing else, check for a simple transition or fall-through.
        last_node = nodes[-1]
        if last_node.get('type') == 'command' and last_node.get('keyword') == 'jump':
            transitions[label_name] = last_node.get('args')
        elif i < len(all_labels) - 1 and label_name not in hubs and label_name not in dispatchers:
            transitions[label_name] = all_labels[i+1]

    # Post-processing to resolve transition chains (unchanged)
    resolved_transitions = OrderedDict()
    for start_label, end_label in transitions.items():
        path, current_label = [start_label, end_label], end_label
        while current_label in transitions and current_label not in hubs and current_label not in dispatchers:
            next_label = transitions[current_label]
            if next_label in path: break
            path.append(next_label); current_label = next_label
        resolved_transitions[start_label] = path[-1]

    return OrderedDict([("hubs", hubs), ("dispatchers", dispatchers), ("transitions", resolved_transitions)])

def main(): # (main is unchanged)
    parser = argparse.ArgumentParser(description="Generate a JSON map of a Ren'Py game's structure from its AST.")
    parser.add_argument("global_ast_path", help="Path to the global_ast.json file.")
    args = parser.parse_args()
    try:
        with open(args.global_ast_path, 'r', encoding='utf-8') as f: hierarchical_ast = json.load(f)
    except FileNotFoundError: print(f"Error: File '{args.global_ast_path}' not found.", file=sys.stderr); sys.exit(1)
    except json.JSONDecodeError: print(f"Error: File '{args.global_ast_path}' is not a valid JSON.", file=sys.stderr); sys.exit(1)
    game_map = analyze_rpy_ast(hierarchical_ast)
    print(json.dumps(game_map, indent=2))

if __name__ == "__main__":
    main()