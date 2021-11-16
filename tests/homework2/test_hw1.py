from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                           get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)


def test_get_longest_diverse_words():
    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write('1 12 123 1234 12345 \n')
        file.write('123456 1234567  12345678 \n')
        file.write('123456789 12345678910 \n')
        file.write('1234567891011 123456789101112')

    assert get_longest_diverse_words('test_file.txt') == ['123456789101112',
                                                          '1234567891011',
                                                          '12345678910',
                                                          '123456789',
                                                          '12345678',
                                                          '1234567',
                                                          '123456',
                                                          '12345',
                                                          '1234',
                                                          '123']


def test_get_rarest_char():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write('qwerty qwerty qwerty z')

    assert get_rarest_char('test_file.txt') == 'z'


def test_count_punctuation_chars():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write('qwerty /  .  , qwerty ()')

    assert count_punctuation_chars('test_file.txt') == 5


def test_count_non_ascii_chars():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        for ord_ in range(120, 135):
            file.writelines(chr(ord_))

    assert count_non_ascii_chars('test_file.txt') == 7


def test_get_most_common_non_ascii_char():

    with open('test_file.txt', mode='w', encoding='unicode-escape') as file:
        file.write(chr(130))
        for ord_ in range(120, 135):
            file.writelines(chr(ord_))

    assert get_most_common_non_ascii_char('test_file.txt') == chr(130)
