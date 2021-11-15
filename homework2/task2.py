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
import sys


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    major_count = -1
    major_elem = None
    minor_count = -1
    minor_elem = None

    for elem in inp:
        elem_count = inp.count(elem)
        if elem_count > major_count or major_count == -1:
            major_count = elem_count
            major_elem = elem
        if elem_count < minor_count or minor_count == -1:
            minor_count = elem_count
            minor_elem = elem

    if not (minor_elem and major_elem):
        sys.exit()
    return major_elem, minor_elem
