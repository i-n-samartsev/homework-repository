"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: s = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def update_str(str_with_backspace: str) -> str:
    string_without_backspace = ""
    for num, letter in enumerate(str_with_backspace):
        if str_with_backspace[num + 1: num + 2] != "#" and letter != "#":
            string_without_backspace += letter
    return string_without_backspace


def backspace_compare(first: str, second: str):
    return update_str(first) == update_str(second)
