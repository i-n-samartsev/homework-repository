from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                           get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)


def test_get_longest_diverse_words():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        lines = ['q q qw qw 1234 \n',
                 'qwe qwe qwer qwer 2345\n',
                 'qwert qwert qwerty qwerty 2345 \n']
        file.writelines(lines)

    assert get_longest_diverse_words('test_file.txt',
                                     encoding='unicode-escape',
                                     quantity=3) == ['qwerty', 'qwert', 'qwer']


def test_get_rarest_char():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write('qwerty qwerty qwerty z')

    assert get_rarest_char('test_file.txt', encoding='unicode-escape') == 'z'


def test_count_punctuation_chars():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write('qwerty /  .  , qwerty ()')

    assert count_punctuation_chars('test_file.txt',
                                   encoding='unicode-escape') == 5


def test_count_non_ascii_chars():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        for ord_ in range(120, 135):
            file.writelines(chr(ord_))

    assert count_non_ascii_chars('test_file.txt',
                                 encoding='unicode-escape') == 7


def test_get_most_common_non_ascii_char():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write(chr(130))
        for ord_ in range(120, 135):
            file.writelines(chr(ord_))
    result = chr(130)
    assert get_most_common_non_ascii_char(file_path='test_file.txt',
                                          encoding='unicode-escape') == result
