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


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    d = {}
    for i in inp:
        if d.get(i, -1) == -1:
            d.update([(i, 1)])
        else:
            d[i] += 1

    k, v = d.popitem()
    max_count = v
    max_value = k
    min_count = v
    min_value = k
    while len(d) > 0:
        k, v = d.popitem()
        if v > max_count:
            max_count = v
            max_value = k
        if v < min_count:
            min_count = v
            min_value = k
    return max_value, min_value
