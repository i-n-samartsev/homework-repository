"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences_in_tuple_list(tree, element: Any):
    ans = 0
    for value in tree:
        if value == element:
            ans += 1
        elif isinstance(value, list) or isinstance(value, tuple):
            ans += find_occurrences_in_tuple_list(value, element)
        elif isinstance(value, dict):
            ans += find_occurrences(value, element)
        elif isinstance(value, set):
            ans += find_occurrences_in_set(value, element)
    return ans


def find_occurrences_in_set(tree: set, element: Any) -> int:
    ans = 0
    while len(tree) > 0:
        value = tree.pop()
        if value == element:
            ans += 1
        elif isinstance(value, list) or isinstance(value, tuple):
            ans += find_occurrences_in_tuple_list(value, element)
        elif isinstance(value, dict):
            ans += find_occurrences(value, element)
        elif isinstance(value, set):
            ans += find_occurrences_in_set(value, element)
    return ans


def find_occurrences(tree: dict, element: Any) -> int:
    ans = 0
    for value in tree.values():
        if value == element:
            ans += 1
        elif isinstance(value, list) or isinstance(value, tuple):
            ans += find_occurrences_in_tuple_list(value, element)
        elif isinstance(value, dict):
            ans += find_occurrences(value, element)
        elif isinstance(value, set):
            ans += find_occurrences_in_set(value, element)
    return ans
