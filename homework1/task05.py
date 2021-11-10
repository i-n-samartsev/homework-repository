"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less
equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    ans = 0
    nums_work = [i for i in nums]
    nums_work.sort(reverse=True)
    for i in range(k):
        if nums_work[i] <= 0:
            break
        ans += nums_work[i]
    return ans
