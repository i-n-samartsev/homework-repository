"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import defaultdict
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    """
    Compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.
    """
    quantity = 0
    first_sums = defaultdict(int)
    for i in a:
        for j in b:
            first_sums[i + j] += 1

    for i in c:
        for j in d:
            if (- i - j) in first_sums:
                quantity += first_sums[- i - j]

    return quantity
