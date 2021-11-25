"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def sort_dict(dictionary):
    sorted_dict = {}
    sorted_keys = sorted(dictionary, key=dictionary.get)
    for key in sorted_keys:
        sorted_dict[key] = dictionary[key]
    return sorted_dict


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    dict_elems = {}
    for elem in inp:
        if dict_elems.get(elem, -1) == -1:
            dict_elems.update([(elem, 1)])
        else:
            dict_elems[elem] += 1

    sort_dict_elem = sort_dict(dict_elems)
    return list(sort_dict_elem.keys())[-1], list(sort_dict_elem.keys())[0]
