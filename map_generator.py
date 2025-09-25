import json
import os
import sys

# Define Ren'Py AST node types for clarity and maintenance
NODE_LABEL = "renpy.ast.Label"
NODE_JUMP = "renpy.ast.Jump"
NODE_MENU = "renpy.ast.Menu"
NODE_IF = "renpy.ast.If"
NODE_SAY = "renpy.ast.Say"
NODE_PASS = "renpy.ast.Pass"

# Define nodes that are considered non-interactive for classification purposes.
# These can precede a jump in a Transition or Dispatcher without changing its type.
NON_INTERACTIVE_NODES = {
    "renpy.ast.Python",
    "renpy.ast.Image",
    "renpy.ast.Show",
    "renpy.ast.Hide",
    "renpy.ast.Scene",
    "renpy.ast.Play",
    "renpy.ast.Stop",
    "renpy.ast.Queue",
    "renpy.ast.With",
    "renpy.ast.UserStatement",
    "renpy.ast.Init",
    NODE_PASS
}

def is_block_pure_jump(block):
    """
    Checks if the last significant node in a block of statements is a Jump.
    This allows for non-interactive setup code before the jump.
    """
    if not block:
        return False
    
    # Iterate backwards to find the last node that isn't non-interactive
    for node in reversed(block):
        if node['type'] in NON_INTERACTIVE_NODES:
            continue
        # The last significant node must be a Jump
        return node['type'] == NODE_JUMP
    
    # If a block only contains non-interactive nodes, it's not a pure jump block
    return False

def is_dispatcher_if(if_node):
    """
    Determines if an If node is purely for dispatching (i.e., all its branches end in a jump).
    """
    # Check the primary 'if' block
    if not is_block_pure_jump(if_node['blocks'][0][1]):
        return False
    
    # Check all subsequent 'elif' blocks
    for _, block in if_node['blocks'][1:]:
        if not is_block_pure_jump(block):
            return False

    # Check the 'else' block if it exists
    if if_node['else'] and not is_block_pure_jump(if_node['else']):
        return False
        
    return True

def get_jumps_from_nodes(nodes):
    """
    Recursively extracts all unique jump targets from a list of AST nodes.
    This is used to find all possible destinations from a label.
    """
    jumps = set()
    if not nodes:
        return jumps
        
    for node in nodes:
        type = node['type']
        
        if type == NODE_JUMP:
            jumps.add(node['target'])
        
        elif type == NODE_IF:
            for _, block in node['blocks']:
                jumps.update(get_jumps_from_nodes(block))
            if node['else']:
                jumps.update(get_jumps_from_nodes(node['else']))
        
        elif type == NODE_MENU:
            for item in node['items']:
                # item is a tuple: (text, condition, block)
                if item[2]:  # If a block of actions exists for the menu item
                    jumps.update(get_jumps_from_nodes(item[2]))
                    
    return jumps

def analyze_label(label_node, filename):
    """
    Analyzes the body of a Label node to classify it and extract metadata.
    This function implements the core classification logic.
    """
    label_name = label_node['name']
    body = label_node['body']
    
    has_menu = False
    has_conditional_jump = False
    has_other_significant_nodes = False
    
    # First pass: identify the types of nodes present in the label's body.
    for node in body:
        type = node['type']
        if type == NODE_MENU:
            has_menu = True
        elif type == NODE_IF and is_dispatcher_if(node):
            has_conditional_jump = True
        # If a node is interactive (like Say) or a complex control structure
        # that doesn't just jump, it's a significant node.
        elif type not in NON_INTERACTIVE_NODES and type != NODE_JUMP:
            has_other_significant_nodes = True

    # Second pass: get all possible jump destinations from this label.
    destinations = get_jumps_from_nodes(body)

    # Third pass: Classify the label based on the nodes found.
    label_type = "Event"  # Default type for standard narrative scenes
    
    if has_menu and has_conditional_jump:
        label_type = "Hybrid"
    elif has_menu:
        label_type = "Hub"
    elif has_conditional_jump and not has_other_significant_nodes:
        label_type = "Dispatcher"
    elif not has_menu and not has_conditional_jump and not has_other_significant_nodes:
        # A block is only a transition if its last significant action is a jump.
        if is_block_pure_jump(body):
            label_type = "Transition"

    return {
        "name": label_name,
        "type": label_type,
        "file": filename,
        "line": label_node['linenumber'],
        "destinations": sorted(list(destinations))
    }

def resolve_target(target, labels_map, visited):
    """
    Recursively follows a chain of 'Transition' labels to find the final,
    non-transition destination. Safely handles cycles.
    """
    if target in visited:
        # Cycle detected, return the start of the cycle to prevent infinite loops
        return target 
    
    if target not in labels_map or labels_map[target]['type'] != 'Transition':
        # This is the final destination (or an unknown label)
        return target

    visited.add(target)
    
    # A valid transition should have exactly one destination
    if not labels_map[target]['destinations']:
        return target # This is a dead-end transition, treat as final
    
    next_target = labels_map[target]['destinations'][0]
    return resolve_target(next_target, labels_map, visited)


# In map_generator.py, delete the existing main() function and replace it with this one.

def main():
    parser = arg.parse.ArgumentParser(description="Generate a JSON map of a Ren'Py game's structure from its AST.")
    parser.add_argument("global_ast_path", help="Path to the global_ast.json file.")
    # Add any other arguments the LLM script might need here if the script fails again.
    args = parser.parse_args()

    try:
        with open(args.global_ast_path, 'r', encoding='utf-8') as f:
            hierarchical_ast = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{args.global_ast_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: File '{args.global_ast_path}' is not a valid JSON.", file=sys.stderr)
        sys.exit(1)

    # --- THE CRITICAL FIX IS HERE ---
    # We call the main analysis function, but we pass it the LIST of nodes
    # from hierarchical_ast['children'], not the top-level dictionary.
    # The name of the main analysis function might be different in your LLM script.
    # If this fails, check the name of the function that does the main work
    # and replace "analyze_rpy_ast" with that name.
    
    # Assuming the main analysis function is called analyze_rpy_ast
    game_map = analyze_rpy_ast(hierarchical_ast) 

    # Print the final, correct JSON output
    print(json.dumps(game_map, indent=2))
    
if __name__ == '__main__':
    main()