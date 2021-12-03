"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree, element: Any):
    if isinstance(tree, set):
        values = list(tree)
    elif isinstance(tree, dict):
        values = tree.values()
    else:
        values = tree
    ans = 0
    for value in values:
        if value == element:
            ans += 1
        elif (
            isinstance(value, list)
            or isinstance(value, tuple)
            or isinstance(value, set)
            or isinstance(value, dict)
        ):
            ans += find_occurrences(value, element)
    return ans
