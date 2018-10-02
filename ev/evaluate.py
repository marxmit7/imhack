from math import log
from mathematics import factorial, permutations, combinations


functions = {
    'log': log,
    'F': factorial,
    'P': permutations,
    'C': combinations
}


def evaluate(expression):
    return eval(expression, functions)
