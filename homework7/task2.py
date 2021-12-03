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

    for letter_f, letter_s in zip(first, second):
        if letter_f == "#" and len(first_change) > 0:
            first_change.pop()
        else:
            first_change.append(letter_f)
        if letter_s == "#" and len(second_change) > 0:
            second_change.pop()
        else:
            second_change.append(letter_s)

    return first_change == second_change
