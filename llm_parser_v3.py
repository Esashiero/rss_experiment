import json
import re

class RenpyParser:
    """
    A parser for a simplified subset of the Ren'py scripting language.
    It builds an Abstract Syntax Tree (AST) from the script content,
    correctly handling nested control flow structures like if-else statements.
    """

    def __init__(self, script_content):
        self.lines = [line for line in script_content.split('\n') if line.strip()]
        self.current_line = 0
        self.ast = {"ast_type": "root", "children": []}

    def get_indentation(self, line):
        """Calculates the indentation level of a given line."""
        return len(line) - len(line.lstrip(' '))

    def parse(self):
        """Starts the parsing process."""
        self.ast["children"] = self.parse_block(0)
        return self.ast

    def parse_block(self, current_indent):
        """
        Recursively parses a block of statements at a given indentation level.
        """
        nodes = []
        while self.current_line < len(self.lines):
            line = self.lines[self.current_line]
            indent = self.get_indentation(line)

            if indent < current_indent:
                # End of the current block
                break

            if indent > current_indent:
                # This indicates a syntax error in a simple parser
                # A new block should only start after a statement that expects one
                # For simplicity, we'll skip this line. A more robust parser would error.
                self.current_line += 1
                continue

            # Process the line at the current indentation level
            node = self.parse_statement(line)
            if node:
                nodes.append(node)
            else:
                # If parse_statement returns None, it means it was handled
                # as part of a larger structure (like 'else'), so we just continue.
                self.current_line += 1
        
        return nodes

    def parse_statement(self, line):
        """Parses a single statement and returns its AST node."""
        stripped_line = line.strip()

        # Check for 'label'
        if stripped_line.startswith("label ") and stripped_line.endswith(":"):
            return self.parse_label(stripped_line)

        # Check for variable assignment
        if stripped_line.startswith("$ "):
            self.current_line += 1
            return {"type": "variable_assignment", "expression": stripped_line}

        # Check for 'menu'
        if stripped_line == "menu:":
            return self.parse_menu()

        # Check for 'if' statement
        if stripped_line.startswith("if ") and stripped_line.endswith(":"):
            return self.parse_if_statement(stripped_line)
        
        # 'else' is handled by parse_if_statement, so if we encounter it here, we skip it.
        if stripped_line == "else:":
            return None

        # Check for dialogue
        dialogue_match = re.match(r'^(\w+)\s+"(.*)"$', stripped_line)
        if dialogue_match:
            self.current_line += 1
            character, text = dialogue_match.groups()
            return {"type": "dialogue", "character": character, "text": text}

        # If no other type matches, assume it's an unhandled line
        return None

    def parse_label(self, line):
        """Parses a label statement and its associated block."""
        name = line.split(" ")[1][:-1]
        self.current_line += 1
        node = {
            "type": "label",
            "name": name,
            "children": self.parse_block(self.get_indentation(self.lines[self.current_line]))
        }
        return node

    def parse_menu(self):
        """Parses a menu statement and its choices."""
        self.current_line += 1
        node = {
            "type": "menu",
            "children": []
        }
        
        # A menu's choices must be more indented than the menu keyword
        menu_indent = self.get_indentation(self.lines[self.current_line -1])
        choice_indent = self.get_indentation(self.lines[self.current_line])

        if choice_indent <= menu_indent:
             return node # Empty menu

        while self.current_line < len(self.lines):
            line = self.lines[self.current_line]
            indent = self.get_indentation(line)
            if indent < choice_indent:
                break # End of menu block
            if indent == choice_indent and line.strip().startswith('"') and line.strip().endswith('":'):
                node["children"].append(self.parse_choice(line.strip()))
            else:
                # This line is not a valid choice, so break from the menu.
                break
        return node
    
    def parse_choice(self, line):
        """Parses a menu choice and its associated block."""
        text = line[1:-2] # Remove quotes and colon
        self.current_line += 1
        
        children = []
        # Check if there is a block associated with this choice
        if self.current_line < len(self.lines):
            choice_indent = self.get_indentation(line)
            next_line_indent = self.get_indentation(self.lines[self.current_line])
            if next_line_indent > choice_indent:
                children = self.parse_block(next_line_indent)

        return {
            "type": "choice",
            "text": text,
            "children": children
        }

    def parse_if_statement(self, line):
        """Parses an if statement, its block, and an optional else block."""
        condition = line.strip().split(" ", 1)[1][:-1]
        self.current_line += 1
        
        node = {
            "type": "if_statement",
            "condition": condition,
            "children": self.parse_block(self.get_indentation(self.lines[self.current_line]))
        }
        
        # Check for a corresponding 'else' statement at the same indentation level
        if self.current_line < len(self.lines):
            if_indent = self.get_indentation(line)
            next_line = self.lines[self.current_line]
            
            if self.get_indentation(next_line) == if_indent and next_line.strip() == "else:":
                self.current_line += 1 # Consume 'else:'
                else_children = self.parse_block(self.get_indentation(self.lines[self.current_line]))
                node["else_block"] = {
                    "type": "else_statement",
                    "children": else_children
                }
        
        return node


# Example .rpy File Content
rpy_content = """
label chapter2_logic:
    $ score = 85
    e "You approach the gatekeeper."
    menu:
        "Bribe the guard":
            if score > 90:
                e "The guard is insulted!"
                $ score -= 10
            else:
                e "The guard accepts the bribe."
                $ bribed_guard = True
        "Persuade the guard":
            e "You make your case."
    e "You are past the gate."
"""

# --- Main Execution ---
if __name__ == "__main__":
    parser = RenpyParser(rpy_content)
    ast = parser.parse()
    
    # Output the resulting JSON
    print(json.dumps(ast, indent=2))