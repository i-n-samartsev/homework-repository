from homework7.hw2 import convert_word


def test_convert_word_strings_with_single_backspace_are_equal():
    assert convert_word('ab#c') == convert_word('ad#c')


def test_convert_word_strings_with_double_backspace_are_equal():
    assert convert_word('a##c') == convert_word('#a#c')


def test_convert_word_strings_with_single_backspace_are_not_equal():
    assert convert_word('a#c') != convert_word('b')


def test_convert_word_empty_strings_are_equal():
    assert convert_word('###') == convert_word('')
