from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    ans = 0
    nums.sort()
    for i in range(k):
        if nums[i] <= 0:
            break
        ans += nums[i]
    return ans
