"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, List


def custom_range(values: List[Any], *args) -> List[Any]:
    ans = []
    if len(args) == 1:
        for val in values:
            if val < args[0]:
                ans.append(val)

    elif len(args) == 2:
        for val in values:
            if args[0] <= val < args[1]:
                ans.append(val)

    elif len(args) == 3:
        if args[2] < 0:
            index_step = 0
            for val in reversed(values):
                if args[1] < val <= args[0] and index_step == 0:
                    ans.append(val)
                index_step += 1
                index_step %= abs(args[2])
        else:
            index_step = 0
            for val in values:
                if args[0] <= val < args[1] and index_step == 0:
                    ans.append(val)
                index_step += 1
                index_step %= abs(args[2])

    return ans
