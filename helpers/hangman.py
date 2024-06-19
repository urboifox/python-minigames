import random

words = words = [
    "and", "as", "assert", "async", "await", "break", "class", "continue", "def", "del", "elif", 
    "else", "except", "False", "finally", "for", "from", "global", "if", "import", "in", "is", 
    "lambda", "None", "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "while", 
    "with", "yield", "abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes", "callable", 
    "chr", "classmethod", "compile", "complex", "delattr", "dict", "dir", "divmod", "enumerate", 
    "eval", "exec", "filter", "float", "format", "frozenset", "getattr", "globals", "hasattr", 
    "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list", 
    "locals", "map", "max", "memoryview", "min", "next", "object", "oct", "open", "ord", "pow", 
    "print", "property", "range", "repr", "reversed", "round", "set", "setattr", "slice", "sorted", 
    "staticmethod", "str", "sum", "super", "tuple", "type", "vars", "zip", "__import__"
]


def get_word() -> str:
    return random.choice(words)


def display_hangman(attempts):
    stages = [  # Final state: head, torso, both arms, and both legs
                """
                   -----
                   |   |
                   O   |
                  /|\\  |
                  / \\  |
                      |
                --------
                """,
                # Head, torso, both arms, and one leg
                """
                   -----
                   |   |
                   O   |
                  /|\\  |
                  /    |
                      |
                --------
                """,
                # Head, torso, and both arms
                """
                   -----
                   |   |
                   O   |
                  /|\\  |
                       |
                       |
                --------
                """,
                # Head, torso, and one arm
                """
                   -----
                   |   |
                   O   |
                  /|   |
                       |
                       |
                --------
                """,
                # Head and torso
                """
                   -----
                   |   |
                   O   |
                   |   |
                       |
                       |
                --------
                """,
                # Head
                """
                   -----
                   |   |
                   O   |
                       |
                       |
                       |
                --------
                """,
                # Initial empty state
                """
                   -----
                   |   |
                       |
                       |
                       |
                       |
                --------
                """
    ]
    print(stages[attempts])