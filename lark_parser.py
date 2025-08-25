import sys
import json
# --- THIS IS THE PERMANENT FIX ---
from lark import Lark, Transformer, v_args
from lark.indenter import Indenter
# ----------------------------------

class RenpyIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

@v_args(inline=True)
class TreeToJson(Transformer):
    def command(self, keyword, args=None):
        return {"type": "command", "keyword": str(keyword), "args": str(args) if args else ""}

    def variable_assignment(self, expression):
        return {"type": "variable_assignment", "expression": f"$ {expression}".strip()}

    def dialogue(self, character, text):
        return {"type": "dialogue", "character": str(character), "text": text.strip('"')}
    
    def return_statement(self, _):
        return {"type": "command", "keyword": "return", "args": ""}

    def args(self, value):
        return value.strip()

    def label(self, name, block):
        return {"type": "label", "name": str(name), "children": block}

    def block(self, *statements):
        return [s for s in statements if s]

    def menu(self, *choices):
        return {"type": "menu", "children": list(choices)}

    def choice(self, text, block):
        return {"type": "choice", "text": text.strip('"'), "children": block}

    def if_statement(self, condition, if_block, *elif_else):
        node = {
            "type": "if_statement",
            "condition": str(condition),
            "children": if_block
        }
        elif_blocks = [item for item in elif_else if item and item.get("type") == "elif_statement"]
        else_block = next((item for item in elif_else if item and item.get("type") == "else_statement"), None)
        if elif_blocks:
            node["elif_blocks"] = elif_blocks
        if else_block:
            node["else_block"] = else_block
        return node

    def elif_statement(self, condition, block):
        return {"type": "elif_statement", "condition": str(condition), "children": block}

    def else_statement(self, block):
        return {"type": "else_statement", "children": block}
    
    def condition(self, value):
        return value.strip()

    def start(self, *statements):
        return {"ast_type": "root", "children": list(statements)}

    # Lark terminals are just strings, so we return them as is
    def IDENTIFIER(self, s):
        return str(s)
    
    def STRING(self, s):
        return str(s)

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <rpy_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    
    with open('renpy_grammar.lark', 'r') as f:
        grammar = f.read()

    with open(input_file, 'r') as f:
        code = f.read()
        
    try:
        parser = Lark(grammar, start='start', parser='lalr', postlex=RenpyIndenter())
        tree = parser.parse(code)
        
        # Transform the Lark Tree into our target JSON format
        json_output = TreeToJson().transform(tree)
        
        print(json.dumps(json_output, indent=2))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()