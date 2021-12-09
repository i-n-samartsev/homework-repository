from string import ascii_lowercase

from homework2.hw5 import custom_range


def test_custom_range_with_only_stop_argument():

    assert custom_range(ascii_lowercase, 'e') == ['a', 'b', 'c', 'd']


def test_custom_range_with_start_and_stop_arguments():

    assert custom_range(ascii_lowercase, 'g', 'k') == ['g', 'h', 'i', 'j']


def test_custom_range_with_start_stop_step_arguments():

    assert custom_range(ascii_lowercase, 'p', 'j', -2) == ['p', 'n', 'l']


def test_custom_range_with_numbers():

    assert custom_range(range(-5, 5), -2, 2) == [-2, -1, 0, 1]
