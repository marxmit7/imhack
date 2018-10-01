from sys import argv as arguments
from pyperclip import copy as copy_to_clipboard
from evaluate import evaluate

USAGE = """\
USAGE :
ev <expression> -> <result>

"""

expression_arguments = arguments[1:]

try:
    expression = ''.join(arguments[1:])
    result = evaluate(expression)
    print(result)
    copy_result = input('Copy to clipboard? ') == 'y'
    if copy_result:
        copy_to_clipboard(result)
except SyntaxError:
    input(USAGE)
