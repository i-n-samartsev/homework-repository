"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string



assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c',
                                                       'd', 'e', 'f']

assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i',
                                                            'j', 'k', 'l',
                                                            'm', 'n', 'o']

assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l',
                                                                'j', 'h']

"""

from typing import Any, List, Sequence


def custom_range(data: Sequence[Any], start: Any, stop: Any = None,
                 step: [int] = 1) -> List[Any]:

    if stop is None:
        start, stop = 0, start

    for i, element in enumerate(data):
        if element == stop:
            stop = i
        elif element == start:
            start = i

    return list(data[start:stop:step])
