from homework1.task02 import check_fibonacci


def test_check_fibonacci():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
                            377, 610, 987, 1597, 2584, 4181, 6765])
    assert not check_fibonacci([0, 1, 1, 2, 6])
