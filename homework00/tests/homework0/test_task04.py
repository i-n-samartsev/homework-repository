from homework0.task04 import check_sum_of_four


def test_regular_case():
    """Testing regular example"""
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 0], [0, 2]) == 4


def test_empty_case():
    """Testing empty lists example"""
    assert check_sum_of_four([], [], [], []) == 0


def test_no_tuple_case():
    """Testing example with no solution tuple"""
    assert check_sum_of_four([1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]) == 0
