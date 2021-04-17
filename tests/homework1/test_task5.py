import pytest

from homework1.task5 import find_maximal_subarray_sum

def test_only_negative_numbers():
    assert find_maximal_subarray_sum([-3,-10,-7, -7],3) == -3

def test_only_positive_numbers():
    assert find_maximal_subarray_sum([4,5,1,7,8,9],3) == 24