from string import ascii_lowercase

from homework2.hw5 import custom_range


def test_1_custom_range():

    assert custom_range(ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']


def test_2_custom_range():

    assert custom_range(ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k',
                                                       'l', 'm', 'n', 'o']


def test_3_custom_range():

    assert custom_range(ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l',
                                                           'j', 'h']
