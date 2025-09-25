# map_generator.py (V10 - With Recursive Nested Menu Parsing)
import json
import argparse
import sys
from collections import OrderedDict

def _flatten_ast(hierarchical_ast):
    flat_ast = OrderedDict()
    for node in hierarchical_ast.get('children', []):
        if node.get('type') == 'label':
            label_name = node.get('name')
            children = node.get('children', [])
            if label_name:
                flat_ast[label_name] = children
    return flat_ast

def _find_first_jump_recursively(node_list):
    for node in node_list:
        if node.get('type') == 'command' and node.get('keyword') == 'jump':
            return node.get('args')
        if 'children' in node:
            found_jump = _find_first_jump_recursively(node.get('children', []))
            if found_jump:
                return found_jump
    return None

def parse_conditional_jumps(nodes):
    paths = []
    cond_nodes = [n for n in nodes if n.get('type') in ('if_statement', 'elif_statement', 'else_statement')]
    for node in cond_nodes:
        condition = "else" if node.get('type') == 'else_statement' else node.get('condition')
        if condition:
            jump_target = _find_first_jump_recursively(node.get('children', []))
            if jump_target:
                paths.append({"condition": condition, "target": jump_target})
    return paths

def is_dispatch_label(nodes):
    has_if = any(n.get('type') == 'if_statement' for n in nodes)
    # --- RECURSIVE CHECK FOR MENU ---
    def has_menu_recursively(node_list):
        for node in node_list:
            if node.get('type') == 'menu': return True
            if 'children' in node and has_menu_recursively(node.get('children', [])): return True
        return False
    # --- END RECURSIVE CHECK ---
    return has_if and not has_menu_recursively(nodes)

def _extract_choices_recursively(menu_node):
    """
    Recursively traverses a menu and its sub-menus to find all possible
    terminal choices (choices that end in a jump). It accumulates conditions
    along each path.
    """
    terminal_choices = OrderedDict()

    def _traverse(node_list, text_path, condition_path):
        # Find the first menu in the current list of nodes
        current_menu = next((n for n in node_list if n.get('type') == 'menu'), None)
        if not current_menu:
            return

        for choice in current_menu.get('children', []):
            if choice.get('type') != 'choice':
                continue

            # Append current choice's text and condition to the path
            new_text_path = text_path + [choice.get('text')]
            new_condition_path = condition_path + [choice.get('condition', "True")]
            
            choice_children = choice.get('children', [])
            jump_target = _find_first_jump_recursively(choice_children)
            nested_menu = next((n for n in choice_children if n.get('type') == 'menu'), None)

            if jump_target:
                # This is a terminal choice. Record it.
                full_choice_text = " -> ".join(new_text_path)
                terminal_choices[full_choice_text] = {
                    "target": jump_target,
                    "conditions": new_condition_path
                }
            elif nested_menu:
                # This is a nested menu. Recurse deeper.
                _traverse(nested_menu.get('children', []), new_text_path, new_condition_path)

    # Start the traversal from the top-level menu node
    _traverse([menu_node], [], [])
    return terminal_choices


def analyze_rpy_ast(hierarchical_ast):
    hubs, transitions, dispatchers = OrderedDict(), OrderedDict(), OrderedDict()
    global_ast = _flatten_ast(hierarchical_ast)
    all_labels = list(global_ast.keys())

    for i, (label_name, nodes) in enumerate(global_ast.items()):
        if not nodes: continue
        
        # --- RECURSIVE CHECK FOR MENU ---
        def find_menu_recursively(node_list):
            for node in node_list:
                if node.get('type') == 'menu': return node
                if 'children' in node:
                    found = find_menu_recursively(node.get('children', []))
                    if found: return found
            return None
        
        menu_node = find_menu_recursively(nodes)
        # --- END RECURSIVE CHECK ---
        
        if menu_node:
            # --- THIS IS THE UPGRADE ---
            choices = _extract_choices_recursively(menu_node)
            # --- END OF UPGRADE ---
            
            if len(choices) > 1:
                # The label is a hub if it has more than one terminal choice path
                hubs[label_name] = {"choices": choices}
                continue
            elif len(choices) == 1:
                # If there's only one path, it's just a complex transition
                transitions[label_name] = list(choices.values())[0]["target"]
                continue

        if is_dispatch_label(nodes):
            paths = parse_conditional_jumps(nodes)
            dispatchers[label_name] = paths
            cond_nodes = [n for n in nodes if n.get('type') in ('if_statement', 'elif_statement', 'else_statement')]
            if cond_nodes:
                last_block_children = cond_nodes[-1].get('children', [])
                has_jump = any(c.get('type') == 'command' and c.get('keyword') == 'jump' for c in last_block_children)
                if not has_jump and i < len(all_labels) - 1:
                    if not any(p['condition'] == 'else' for p in paths):
                        paths.append({"condition": "else", "target": all_labels[i + 1]})
            continue

        last_node = nodes[-1]
        if last_node.get('type') == 'command' and last_node.get('keyword') == 'jump':
            transitions[label_name] = last_node.get('args')
        elif i < len(all_labels) - 1 and label_name not in hubs and label_name not in dispatchers:
            transitions[label_name] = all_labels[i+1]

    resolved_transitions = OrderedDict()
    for start_label, end_label in transitions.items():
        path, current_label = [start_label, end_label], end_label
        while current_label in transitions and current_label not in hubs and current_label not in dispatchers:
            next_label = transitions[current_label]
            if next_label in path: break
            path.append(next_label)
            current_label = next_label
        resolved_transitions[start_label] = path[-1]

    return OrderedDict([("hubs", hubs), ("dispatchers", dispatchers), ("transitions", resolved_transitions)])

def main():
    parser = argparse.ArgumentParser(description="Generate a JSON map of a Ren'Py game's structure from its AST.")
    parser.add_argument("global_ast_path", help="Path to the global_ast.json file.")
    args = parser.parse_args()
    try:
        with open(args.global_ast_path, 'r', encoding='utf-8') as f: hierarchical_ast = json.load(f)
    except FileNotFoundError: print(f"Error: The file '{args.global_ast_path}' was not found.", file=sys.stderr); sys.exit(1)
    except json.JSONDecodeError: print(f"Error: The file '{args.global_ast_path}' is not a valid JSON file.", file=sys.stderr); sys.exit(1)
    game_map = analyze_rpy_ast(hierarchical_ast)
    print(json.dumps(game_map, indent=2))

if __name__ == "__main__":
    main()