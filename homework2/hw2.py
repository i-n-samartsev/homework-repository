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
    """This function find the most common and the least common element in "inp".
     Array must be non-empty and the most common element always exist in the
     array."""
    most_common = least_common = None, 0
    for uniq_obj in set(inp):
        number_of_obj = uniq_obj, inp.count(uniq_obj)
        if number_of_obj[1] >= most_common[1]:
            most_common = number_of_obj
        if number_of_obj[1] < least_common[1]:
            least_common = number_of_obj
    return most_common[0], least_common[0]
