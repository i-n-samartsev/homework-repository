"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
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


def find_occurrences(tree: dict, element: Any) -> int:
    """
        Takes an element and finds the number of occurrences of this
        element in the tree.

        Tree can only contains basic structures like:
        str, list, tuple, dict, set, int, bool
    """
    occurrences = 0

    def get_all_children(root):
        nonlocal occurrences
        if isinstance(root, dict):
            for key, value in root.items():
                occurrences += key == element
                get_all_children(root=value)
        elif isinstance(root, (list, tuple, set)):
            for item in root:
                get_all_children(root=item)
        else:
            occurrences += root == element

    get_all_children(tree)
    return occurrences


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
