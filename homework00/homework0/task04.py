"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import defaultdict
from typing import List


def check_sum_of_four(a: List[int],
                      b: List[int],
                      c: List[int],
                      d: List[int]) -> int:
    hash_map = defaultdict()
    for a_item in a:
        for b_item in b:
            if a_item + b_item not in hash_map:
                hash_map[a_item + b_item] = 1
            else:
                hash_map[a_item + b_item] += 1

    res = 0
    for c_item in c:
        for d_item in d:
            if -(c_item + d_item) in hash_map:
                res += hash_map[-(c_item + d_item)]
    return res
