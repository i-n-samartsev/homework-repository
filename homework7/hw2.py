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
from typing import Generator
from timeit import timeit
from functools import partial


def reversed_converted_word(word: str) -> Generator:
    """
        Converts a string, considering that # is a backspace character.
        Returns reversed result string.
    """
    backspaces = 0
    word = iter(reversed(word))
    for char in word:
        if char == '#':
            backspaces += 1
        else:
            if backspaces:
                backspaces -= 1
                continue
            yield char


def convert_word(word: str) -> str:
    """
        Converts a string, considering that # is a backspace character.
    """
    transformed_word = ''
    for char in word:
        if char == '#':
            transformed_word = transformed_word[:-1]
        else:
            transformed_word += char
    return transformed_word


def backspace_compare(first: str, second: str) -> bool:
    """
        Takes two strings. Return if they are equal when both are typed into
        empty text editors. # means a backspace character.
    """
    return convert_word(first) == convert_word(second)


def backspace_compare_with_generator(first: str, second: str) -> bool:
    """
        Takes two strings. Return if they are equal when both are typed into
        empty text editors. # means a backspace character.
    """
    first, second = map(reversed_converted_word, (first, second))
    return ''.join(first) == ''.join(second)


if __name__ == '__main__':
    words = ('ab#c' * 10000, 'ad#c' * 10000)
    backspace_compare = partial(backspace_compare, *words)
    backspace_compare_with_generator = partial(
        backspace_compare_with_generator, *words)

    print(timeit(backspace_compare, number=100))
    print(timeit(backspace_compare_with_generator, number=100))
