from pytest import raises

from homework9.hw2 import Supressor, supressor


def test_supressor_class_suppresses_its_exception():
    with Supressor(IndexError):
        [][10]


def test_supressor_class_does_not_suppresses_another_exception():
    with raises(IndexError):
        with Supressor(ValueError):
            [][10]


def test_supressor_function_suppresses_its_exception():
    with supressor(ZeroDivisionError):
        1/0


def test_supressor_function_does_not_suppresses_another_exception():
    with raises(ZeroDivisionError):
        with supressor(ValueError):
            1/0
