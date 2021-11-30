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


def backspace_compare(first: str, second: str):
    first_change = []
    second_change = []

    for letter in first:
        if letter == "#" and len(first_change) > 0:
            first_change.pop()
        else:
            first_change += letter
    for letter in second:
        if letter == "#" and len(second_change) > 0:
            second_change.pop()
        else:
            second_change += letter

    return first_change == second_change
