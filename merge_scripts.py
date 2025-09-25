# merge_scripts.py
import os
import sys

def merge_rpy_files(game_dir, output_file):
    """
    Finds all .rpy files in a directory, sorts them, and concatenates
    them into a single output file.
    """
    if not os.path.isdir(game_dir):
        print(f"Error: Directory '{game_dir}' not found.", file=sys.stderr)
        return

    rpy_files = []
    for root, _, files in os.walk(game_dir):
        for file in files:
            if file.endswith(".rpy"):
                rpy_files.append(os.path.join(root, file))
    
    # Sort the files alphabetically. This is a common and usually safe
    # way to handle Ren'Py script loading order.
    rpy_files.sort()

    print(f"Found {len(rpy_files)} .rpy files. Merging into '{output_file}'...")

    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for filepath in rpy_files:
                outfile.write(f"\n# --- Start of file: {os.path.basename(filepath)} ---\n")
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    print(f"Warning: Could not read {filepath}. Error: {e}", file=sys.stderr)
                outfile.write(f"\n# --- End of file: {os.path.basename(filepath)} ---\n")
        
        print(f"Successfully created '{output_file}'.")
    except Exception as e:
        print(f"Error writing to '{output_file}': {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_scripts.py <game_directory> <output_filename>")
        sys.exit(1)
        
    game_directory = sys.argv[1]
    output_filename = sys.argv[2]
    
    merge_rpy_files(game_directory, output_filename)