import sys
import json
from lark import Lark, Transformer, Indenter

class RenpyIndenter(Indenter):
    NL_type = '_NEWLINE'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

class TreeToJson(Transformer):
    def transform(self, tree):
        # This will be our logic to convert Lark's tree to our specific JSON
        return super().transform(tree)

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
        
        # For now, we just print the raw tree.
        # We will convert it to our JSON format in the next step.
        print(tree.pretty())

    except Exception as e:
        print(f"Error parsing file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()