# find_label.py
import sys

def find_label_in_file(filepath, label_name, lines_after=50):
    """
    Searches for a specific label in a file and prints the subsequent lines.
    This is more robust than grep for files with mixed line endings.
    """
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return

    target_line = f"label {label_name}"
    
    for i, line in enumerate(lines):
        # We strip the line to handle potential leading whitespace
        if line.strip().startswith(target_line):
            print(f"--- Found '{target_line}' at line {i+1} ---")
            
            # Print the label line and the next N lines
            start_index = i
            end_index = min(i + 1 + lines_after, len(lines))
            
            for j in range(start_index, end_index):
                # Print with line numbers for context
                print(f"{j+1:05d}: {lines[j].strip()}")
            
            print("--- End of Snippet ---")
            return # Stop after finding the first match

    print(f"Error: Label '{label_name}' not found in the file.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find_label.py <path_to_rpy_file> <label_name>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    label_to_find = sys.argv[2]
   
    find_label_in_file(file_path, label_to_find)
