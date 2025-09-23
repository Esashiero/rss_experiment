import json
import sys

def find_nodes(node, search_criteria, path=""):
    """
    Recursively searches the AST for nodes that match specific criteria.
    
    Args:
        node: The current node (dict or list) to search within.
        search_criteria: A function that returns True if a node matches.
        path: The current path in the AST (for context).
        
    Returns:
        A list of (matching_node, path) tuples.
    """
    results = []
    
    # If the current node is a dictionary
    if isinstance(node, dict):
        # Check if the current node itself matches the criteria
        if search_criteria(node):
            results.append((node, path))
        
        # Recurse into its children
        for key, value in node.items():
            new_path = f"{path} -> {key}"
            results.extend(find_nodes(value, search_criteria, new_path))
            
    # If the current node is a list
    elif isinstance(node, list):
        for index, item in enumerate(item for item in node):
            new_path = f"{path}[{index}]"
            results.extend(find_nodes(item, search_criteria, new_path))
            
    return results

def main():
    if len(sys.argv) < 3:
        print("Usage:", file=sys.stderr)
        print(f"  python {sys.argv[0]} <ast_file> label <label_name>", file=sys.stderr)
        print(f"  python {sys.argv[0]} <ast_file> condition <text_in_condition>", file=sys.stderr)
        sys.exit(1)

    ast_path = sys.argv[1]
    search_type = sys.argv[2]
    search_term = " ".join(sys.argv[3:])

    try:
        with open(ast_path, 'r') as f:
            ast = json.load(f)
    except Exception as e:
        print(f"Error loading AST file: {e}", file=sys.stderr)
        return

    print(f"--- Inspecting AST for '{search_type}' containing '{search_term}' ---")
    
    criteria = None
    if search_type == "label":
        criteria = lambda node: node.get("type") == "label" and search_term in node.get("name", "")
    elif search_type == "condition":
        criteria = lambda node: "condition" in node and search_term in node["condition"]
    else:
        print(f"Error: Unknown search type '{search_type}'", file=sys.stderr)
        return

    found_nodes = find_nodes(ast, criteria, "root")

    if not found_nodes:
        print("\nNo matching nodes found.")
    else:
        print(f"\nFound {len(found_nodes)} matching node(s):")
        for node, path in found_nodes:
            print("\n" + "="*40)
            print(f"Found at Path: {path}")
            print("Node Content:")
            print(json.dumps(node, indent=2))
            print("="*40)

if __name__ == "__main__":
    main()