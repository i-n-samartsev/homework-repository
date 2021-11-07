from homework0.task05 import find_maximal_subarray_sum


def test_regular_case():
    """Testing regular example"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 16


def test_k1_case():
    """Testing k = 1 example"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 1) == 7


def test_k0_case():
    """Testing k = 0 example"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 0) == 0


def test_empty_case():
    """Testing empty example"""
    assert find_maximal_subarray_sum([], 1) == 0
