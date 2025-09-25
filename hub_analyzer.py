# hub_analyzer.py (V2 - with Recursive Search)

import json
import sys

def _extract_choices_from_menu(menu_node):
    """Helper function to extract all choice data from a menu node."""
    choices = []
    for choice_node in menu_node.get('children', []):
        if choice_node.get('type') == 'choice':
            choice_text = choice_node.get('text', 'Unknown Choice')
            target_label = None
            # Find the 'jump' command within the choice's actions
            for action_node in choice_node.get('children', []):
                if action_node.get('type') == 'command' and action_node.get('keyword') == 'jump':
                    target_label = action_node.get('args')
                    break  # Found the jump, no need to look further

            if target_label:
                choices.append({
                    "text": choice_text,
                    "target_label": target_label
                })
    return choices

def _find_menu_recursively(node_list):
    """
    Recursively searches a list of nodes and their children for the first
    'menu' node it can find.
    """
    for node in node_list:
        if node.get('type') == 'menu':
            return node # Found it

        # If the node is a container (like if/elif/else), search its children
        if 'children' in node:
            found_menu = _find_menu_recursively(node.get('children', []))
            if found_menu:
                return found_menu # Propagate the found menu up the chain

    return None # Found nothing in this branch

def get_hub_choices(ast, hub_label):
    """
    Performs a targeted, deep parse of a given hub_label from the AST to
    extract all available menu choices, searching inside conditional blocks.

    Args:
        ast (dict): The global Abstract Syntax Tree of the game.
        hub_label (str): The specific label to analyze (e.g., 'saturdaymorning').

    Returns:
        list: A list of dictionaries representing player choices.
    """
    # Find the specific label node in the AST
    hub_node = next((node for node in ast.get('children', [])
                     if node.get('type') == 'label' and node.get('name') == hub_label), None)

    if not hub_node:
        return []

    # NEW: Perform a deep, recursive search for a menu within the hub's children
    menu_node = _find_menu_recursively(hub_node.get('children', []))

    if menu_node:
        return _extract_choices_from_menu(menu_node)

    # If no menu is found after a deep search, return empty.
    return []