from homework1.task04 import check_sum_of_four
from random import randint
from itertools import product
from typing import List


def check_sum_with_product(a: List[int], b: List[int],
                           c: List[int], d: List[int]) -> int:
    """
    Compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero with function 'product'.
    """
    sums_with_product = [sum(item) for item in product(a, b, c, d)]
    return sums_with_product.count(0)


def test_check_sum_of_four_on_a_random_data():
    data = []
    for _ in range(4):
        data.append([randint(0, 100), randint(0, 100)])
    assert check_sum_of_four(*data) == check_sum_with_product(*data)


def test_check_sum_of_four_on_a_monotonous_data():
    data = []
    for _ in range(4):
        data.append([0, 0])
    assert check_sum_of_four(*data) == check_sum_with_product(*data)
