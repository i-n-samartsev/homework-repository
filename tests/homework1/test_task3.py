from homework1.task03 import find_maximum_and_minimum


def test1():
    """"Test file consist only one value one line"""
    assert find_maximum_and_minimum("tests/homework1/test_files_task3/test1.txt") == (1, 1)


def test2():
    """"Test file consist two equal values"""
    assert find_maximum_and_minimum("tests/homework1/test_files_task3/test2.txt") == (5, 5)


def test3():
    """"Test file consist two equal values"""
    assert find_maximum_and_minimum("tests/homework1/test_files_task3/test3.txt") == (-2, 40)