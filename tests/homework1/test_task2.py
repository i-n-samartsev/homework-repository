from homework1.task02 import check_fibonacci


def test1():
    """"Checking is sequence empty or not"""
    assert not check_fibonacci([])


def test2():
    """"Checking first element of fibonacci sequence"""
    assert check_fibonacci([0])


def test3():
    """"Checking first two elements of fibonacci sequence"""
    assert check_fibonacci([0, 1])


def test4():
    """"Checking first three element of fibonacci sequence"""
    assert check_fibonacci([0, 1, 1])


def test5():
    """"Checking correct fibonacci sequence"""
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])


def test6():
    """"Checking wrong fibonacci sequence"""
    assert not check_fibonacci([0, 1, 1, 2, 4, 5, 8, 13, 21, 34, 55])
