from itertools import product

from homework2.hw3 import combinations


def test_combinations_with_one_list():
    data = [[1, 2]]
    assert combinations(*data) == list(map(list, product(*data)))


def test_combinations_with_three_lists():
    data = [[1, 2], [0], [3, 4]]
    assert combinations(*data) == list(map(list, product(*data)))


def test_combinations_with_empty_data():
    data = []
    assert combinations(*data) == list(map(list, product(*data)))
