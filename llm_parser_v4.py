import json
import re

class RenpyParser:
    """
    A corrected parser for a simplified subset of the Ren'py scripting language.
    It builds an Abstract Syntax Tree (AST) and now correctly handles if-else
    statements, ensuring the 'else_block' is properly structured and the
    'if' condition is clean.
    """

    def __init__(self, script_content):
        # Filter out empty lines from the script
        self.lines = [line for line in script_content.split('\n') if line.strip()]
        self.current_line = 0
        self.ast = {"ast_type": "root", "children": []}

    def get_indentation(self, line):
        """Calculates the number of leading spaces to determine indentation level."""
        return len(line) - len(line.lstrip(' '))

    def parse(self):
        """Initiates the parsing process from the top level."""
        # The root of the document is a block at indentation 0
        self.ast["children"] = self.parse_block(0)
        return self.ast

    def parse_block(self, current_indent):
        """
        Recursively parses a block of statements defined by a specific indentation.
        A block ends when a line with less indentation is encountered.
        """
        nodes = []
        while self.current_line < len(self.lines):
            line = self.lines[self.current_line]
            indent = self.get_indentation(line)

            if indent < current_indent:
                # This line is less indented, so it's the end of the current block.
                break

            if indent > current_indent:
                # This would be a syntax error in a real script, as a new block
                # must be preceded by a statement that allows it (if, menu, etc.).
                # We'll skip it to prevent infinite loops.
                self.current_line += 1
                continue

            # This line is at the correct indentation for the current block.
            node = self.parse_statement(line)
            if node:
                # A statement can return multiple nodes if it's a compound
                # statement like if-else, but our logic handles that internally.
                nodes.append(node)
            else:
                # If parse_statement returns None (e.g., for an 'else' that was
                # already consumed by 'if'), just advance the line counter.
                self.current_line += 1
        
        return nodes

    def parse_statement(self, line):
        """Determines the type of a single statement and calls the correct parser."""
        stripped_line = line.strip()

        if stripped_line.startswith("label ") and stripped_line.endswith(":"):
            return self.parse_label(line)
        
        if stripped_line.startswith("$ "):
            self.current_line += 1
            return {"type": "variable_assignment", "expression": stripped_line}

        if stripped_line == "menu:":
            return self.parse_menu(line)

        if stripped_line.startswith("if ") and stripped_line.endswith(":"):
            # This is the corrected logic for if-else.
            return self.parse_if_statement(line)
        
        # This is the key fix: 'else' is handled by 'parse_if_statement'.
        # If we encounter it here, it means it's an 'else' without an 'if',
        # so we can ignore it or treat it as an error. Here we return None.
        if stripped_line == "else:":
            return None

        dialogue_match = re.match(r'^(\w+)\s+"(.*)"$', stripped_line)
        if dialogue_match:
            self.current_line += 1
            character, text = dialogue_match.groups()
            return {"type": "dialogue", "character": character, "text": text}

        # Return None for any line that doesn't match a known pattern.
        return None

    def parse_label(self, line):
        name = line.strip().split(" ")[1][:-1]
        self.current_line += 1
        # A label introduces a new, more indented block.
        children = self.parse_block(self.get_indentation(self.lines[self.current_line]))
        return {"type": "label", "name": name, "children": children}

    def parse_menu(self, line):
        self.current_line += 1
        menu_indent = self.get_indentation(line)
        # The choices in a menu must be more indented than the 'menu:' keyword.
        children = self.parse_block(menu_indent + 1)
        return {"type": "menu", "children": children}

    def parse_choice(self, line):
        text = line.strip()[1:-2]  # Remove quotes and colon
        self.current_line += 1
        children = []
        # Check if the choice is followed by an indented block.
        if self.current_line < len(self.lines):
            choice_indent = self.get_indentation(line)
            next_line_indent = self.get_indentation(self.lines[self.current_line])
            if next_line_indent > choice_indent:
                children = self.parse_block(next_line_indent)
        return {"type": "choice", "text": text, "children": children}

    def parse_if_statement(self, line):
        """
        Parses an 'if' statement, its children, and actively looks for a
        subsequent 'else' block at the same indentation level.
        """
        # FIX: Correctly extract the condition without the "if" keyword or colon.
        condition = line.strip()[3:-1]
        self.current_line += 1
        
        node = {
            "type": "if_statement",
            "condition": condition,
            "children": self.parse_block(self.get_indentation(self.lines[self.current_line]))
        }
        
        # FIX: After parsing the 'if' block, check if the *next* line is an 'else'.
        if self.current_line < len(self.lines):
            if_indent = self.get_indentation(line)
            next_line = self.lines[self.current_line]
            
            # The 'else' must be at the same indentation level as the 'if'.
            if self.get_indentation(next_line) == if_indent and next_line.strip() == "else:":
                self.current_line += 1  # Consume the 'else:' line.
                # Parse the block belonging to the 'else'.
                else_children = self.parse_block(self.get_indentation(self.lines[self.current_line]))
                node["else_block"] = {
                    "type": "else_statement",
                    "children": else_children
                }
        
        return node


# --- Main Execution: Test with the specific debugging case ---
if __name__ == "__main__":
    # The input code provided in the debugging task.
    rpy_code_snippet = """
if score > 90:
    e "The guard is insulted!"
else:
    e "The guard accepts the bribe."
"""

    # Instantiate the parser with the corrected logic.
    parser = RenpyParser(rpy_code_snippet)
    
    # The parse_block method returns a list of nodes. Since our input
    # is a single if-else statement, we expect a list with one item.
    ast_nodes = parser.parse()["children"]
    
    # Get the first (and only) top-level node.
    if ast_nodes:
        single_if_node = ast_nodes[0]
        # Output the resulting JSON, which should match the required format.
        print(json.dumps(single_if_node, indent=2))
    else:
        print("Parsing failed to produce any nodes.")