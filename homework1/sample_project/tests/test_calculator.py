import pytest

from homework1.sample_project.calculator.calc import check_power_of_2


def test_true_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)
    
def test_false_case():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)

def test_zero_number_case():
    """Testing that 0 number gives False"""
    assert not check_power_of_2(0)

def test_negative_number_case():
    """Testing that negative numbers give False"""
    assert not check_power_of_2(-5)

def test_one_number_case():
    """Testing that 1-power of 2 gives True"""
    assert check_power_of_2(1)

