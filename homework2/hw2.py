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
from collections import Counter
from dataclasses import dataclass
from typing import Any, List


@dataclass
class MajorMinorElements:
    major_elem: Any
    number_of_major_elem: int
    minor_elem: Any
    number_of_minor_elem: int


def major_and_minor_elem(inp: List) -> MajorMinorElements:
    """
    Find the most common and the least common elements.
    Returns MajorMinorElements object.
    """
    elements = Counter(inp).most_common()
    most_common = elements[0]
    least_common = elements[-1]
    return MajorMinorElements(*most_common, *least_common)
