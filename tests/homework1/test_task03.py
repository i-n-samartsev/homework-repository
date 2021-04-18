"""Tests for task03 - Min&max"""

from homework1.task03 import find_maximum_and_minimum


def test_min_max():
    """Testing that file.txt will be read
    and min and max values will be returned
    as a tuple"""
    assert (
        find_maximum_and_minimum(
            r"C:\Users\User\EPAM\
    homework-repository\homework1\test_task3_1.txt"
        )
        == (-2000, 2000)
    )


def test_with_one_line():
    """Testing that file.txt will be read
    and min and max values will be returned
    as a tuple for one line"""
    assert (
        find_maximum_and_minimum(
            r"C:\Users\User\EPAM\
    homework-repository\homework1\test_task3_2.txt"
        )
        == (5, 5)
    )
