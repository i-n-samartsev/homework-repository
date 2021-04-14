"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def _combinations(*args: List[Any]) -> List[List]:
    """This function returns all possible k-combinations (k = number of lists)
        of values from input lists. All combinations splitting by 2-3 values per
        lists. They needed processing"""
    k = len(args)
    all_combo = []
    if k == 2:
        for list1_elem in args[0]:
            for list2_elem in args[1]:
                all_combo.append([list1_elem, list2_elem])
        return all_combo
    if k == 3:
        for list1_elem in args[0]:
            for list2_elem in args[1]:
                for list3_elem in args[2]:
                    # faster then invent a function :).
                    all_combo.extend([[list1_elem, list2_elem, list3_elem],
                                      [list1_elem, list3_elem, list2_elem],
                                      ])
        return all_combo
    return _combinations(_combinations(*args[:k // 2]),
                         _combinations(*args[k // 2:]))


def combinations(*args: List[Any]) -> List[List]:
    """This function takes K lists as arguments and returns all possible
        lists of K items where the first element is from the first list,
        the second is from the second and so one."""
    combos = []
    for combo in _combinations(*args):
        while len(combo) != len(args):
            tmp_elem = []
            for elem in combo:
                tmp_elem.extend(elem)
            combo = tmp_elem
            del tmp_elem
        combos.append(combo)
    return combos
