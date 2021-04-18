"""Tests for task02_var1 - Fibonacci"""

from homework1.task02_var1 import check_fibonacci


def test_positive_amount_of_elem():
    """Testing that sequence contains enough elements (return True)"""
    assert check_fibonacci([0, 1, 1])


def test_negative_amount_of_elem():
    """Testing that sequence doesn't contain enough elements (return False)"""
    assert not check_fibonacci([0])


def test_positive_start_fibonacci():
    """Testing that sequence starts like the Fibonacci sequence (return True)"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8])


def test_negative_start_fibonacci():
    """Testing that sequence starts like the Fibonacci sequence (return False)"""
    assert not check_fibonacci([1, 1, 2, 3, 5, 8])


def test_positive_is_fibonacci():
    """Testing that all the sequence is the Fibonacci sequence (return True)"""
    assert check_fibonacci([0, 1, 1, 2])


def test_negative_is_fibonacci():
    """Testing that all the sequence isn't the Fibonacci sequence (return False)"""
    assert not check_fibonacci([0, 1, 1, 2, 3, 5, 8, 12])
