"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from collections.abc import Iterable, Mapping
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(obj: Any, element: Any) -> int:
    """
        Takes an element and finds the number of occurrences of this
        element in the tree.

        Tree can only contains basic structures like:
        str, list, tuple, dict, set, int, bool
    """
    occurrences = 0

    if isinstance(obj, Mapping):
        for key, value in obj.items():
            occurrences += find_occurrences(obj=key, element=element)
            occurrences += find_occurrences(obj=value, element=element)
    elif isinstance(obj, Iterable) and not isinstance(obj, str):
        for item in obj:
            occurrences += find_occurrences(obj=item, element=element)
    else:
        occurrences += obj == element
    return occurrences


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
