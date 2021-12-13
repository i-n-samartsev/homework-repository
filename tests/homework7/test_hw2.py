from homework7.hw2 import backspace_compare


def test_backspace_compare_strings_with_single_backspace_are_equal():
    assert backspace_compare('ab#c', 'ad#c') is True


def test_backspace_compare_strings_with_double_backspace_are_equal():
    assert backspace_compare('abcd#e###c', '#aa#c') is True


def test_backspace_compare_strings_with_single_backspace_are_not_equal():
    assert backspace_compare('a#c', 'b') is False


def test_backspace_compare_different_length_strings_are_not_equal():
    assert backspace_compare('abc', 'bc') is False


def test_backspace_compare_empty_strings_are_equal():
    assert backspace_compare('###', '') is True
