"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """"
    This function check the given sequence is a sequence of fibonacci or not
    """
    if not data:
        return False
    first = data[0]
    if first != 0:
        return False
    if len(data) > 1:
        second = data[1]
        if second != 1:
            return False
    for element in data[2:]:
        if element != first+second:
            return False
        first, second = second, element
    return True
