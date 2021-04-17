import pytest

from homework1.task4 import check_sum_of_four

def test_positive():
    assert check_sum_of_four([3,-4,0],[-7,4,0],[0,-5,1],[0,8,-4]) == 4

def test_only_zero():
    assert check_sum_of_four([0,0], [0,0], [0,0], [0,0]) == 16

def test_no_zero():
    assert check_sum_of_four([10,20,9], [3,4,6], [56,2,3], [8,9,10]) == 0