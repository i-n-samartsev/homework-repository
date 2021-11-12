import os

from homework1.task03 import find_maximum_and_minimum


def test_find_maximum_and_minimum():
    assert find_maximum_and_minimum(
        os.getcwd() + "/homework1/" + "test_task03_data.txt"
    ) == (3, 56)
