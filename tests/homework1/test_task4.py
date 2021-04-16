from homework1.task04 import check_sum_of_four


def test1():
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test2():
    assert check_sum_of_four([0, 1], [0, -1], [0, 1], [0, -1]) == 6
