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

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest
from typing import Generator


def convert_word(word: str) -> Generator:
    """
        Converts a string, considering that # is a backspace character.
        Returns reversed resulting string.
    """
    backspaces = 0
    for char in reversed(word):
        if char == '#':
            backspaces += 1
        else:
            if backspaces:
                backspaces -= 1
                continue
            yield char


def backspace_compare(first: str, second: str) -> bool:
    """
        Takes two strings. Return if they are equal when both are typed into
        empty text editors. # means a backspace character.
    """
    first_word, second_word = map(convert_word, (first, second))
    return all(i == j for i, j in zip_longest(first_word, second_word))
