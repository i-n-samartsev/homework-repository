import pytest

from homework1.task2 import check_fibonacci

def test_fibonacci_sequence():
    assert check_fibonacci([55, 89, 144])

def test_not_fibonacci_sequence():
    assert check_fibonacci([56, 78, -10])