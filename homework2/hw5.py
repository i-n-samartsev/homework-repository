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


def custom_range(data: Sequence[Any], *args: (Any, Any, int)) -> List[Any]:
    """
    Returns a subarray from the passed sequence.
    Examples of application:

    custom_range(data, elem) --> subarray from beginning to 'elem'

    custom_range(data, elem1, elem2) --> subarray from 'elem1' to 'elem2'

    custom_range(data, elem1, elem2, step) --> subarray from 'elem1' to
    'elem2' with 'step'
    """
    if 0 >= len(args) > 3:
        raise ValueError('Wrong number of parameters')

    start = data.index(args[0]) if len(args) > 1 else 0
    stop = data.index(args[1]) if len(args) > 1 else data.index(args[0])
    step = args[2] if len(args) == 3 else 1
    return list(data[start:stop:step])
