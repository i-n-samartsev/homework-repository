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
    for i in range(1, k + 1):
        for j in range(len(nums)):
            sum_nums = 0
            for q in range(i):
                if j + q > len(nums) - 1:
                    break
                sum_nums += nums[j + q]
            if ans < sum_nums:
                ans = sum_nums
    if ans == 0:
        return max(nums)
    return ans
