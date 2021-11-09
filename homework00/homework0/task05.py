"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List

""" Find a sub-array with length less or equal to "k" """


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k or k == 0:
        return 0

    res = 0
    for j in range(1, k + 1):
        sum = 0
        for i in range(j):
            sum += nums[i]

        for i in range(j, len(nums)):
            sum += nums[i] - nums[i-j]
            res = max(res, sum)

    return res


""" Find a sub-array with length equal to "k"
def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k or k == 0:
        return 0

    sum = 0
    for i in range(k):
        sum += nums[i]

    res = 0
    for i in range(k, len(nums)):
        sum += nums[i] - nums[i-k]
        res = max(res, sum)

    return res
"""
