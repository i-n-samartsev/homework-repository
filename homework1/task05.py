"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Find a sub-array with length less equal to 'k', with maximal sum.
    """
    if len(nums) == 0:
        raise ValueError('Sequence is empty')
    if k <= 0:
        raise ValueError('Parameter "k" must be > 0')

    subarrays = []
    for subarray_size in range(1, k + 1):
        for i in range(len(nums) - subarray_size + 1):
            subarrays.append(nums[i:i + subarray_size])
    return max(map(sum, subarrays))
