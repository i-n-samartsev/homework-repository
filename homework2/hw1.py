"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from collections import Counter
from typing import List
from unicodedata import category
from dataclasses import dataclass


@dataclass
class Token:
    kind: str
    value: str


def file_opener_1(file_path: str, mode: str = 'r', encoding: str = 'utf8',
                  errors: str = 'strict'):
    with open(file_path, mode=mode, encoding=encoding, errors=errors) as file:
        return file


def file_opener_2(file_path: str, mode: str = 'r', encoding: str = 'utf8',
                  errors: str = 'strict'):
    try:
        file = open(file_path, mode=mode, encoding=encoding, errors=errors)
        return file
    finally:
        file.close()




def awesome_parse(path_or_file):
    if isinstance(path_or_file, basestring):
        f = file_to_close = open(path_or_file, 'rb')
    else:
        f = path_or_file
        file_to_close = None
    try:
        return do_stuff(f)
    finally:
        if file_to_close:
            file_to_close.close()


def tokenize(open_file):
    buffer = ''
    for symbol in open_file:
        if category(symbol).startswith('L'):
            buffer += symbol
        else:
            if buffer:
                yield Token(kind='word', value=buffer)
                buffer = ''
            yield Token(kind='symbol', value=symbol)


def get_longest_diverse_words(file_path: str, encoding: str = 'utf8',
                              errors: str = 'strict') -> List[str]:
    words_stat = {}
    file = file_opener(file_path, encoding=encoding, errors=errors)
    print(file.closed)
    for word in tokenize(file):
        print(word)


get_longest_diverse_words('data.txt', encoding='unicode_escape',
                          errors='ignore')

    # with open(file_path, mode='r', encoding='unicode-escape',
    #           errors='ignore') as file:
    #     for line in file:
    #         words = line.split()
    #         for word in words:
    #             words_stat[len(word)].append(word.strip(string.punctuation))
    #
    # sorted_length = sorted(words_stat, reverse=True)
    # answer = []
    #
    # for length in sorted_length:
    #     if not words_stat[length]:
    #         continue
    #     answer.append(words_stat[length].pop())
    #     if len(answer) > 9:
    #         break
    #
    # return answer


def get_rarest_char(file_path: str) -> str:
    chars_stat = Counter()

    with open(file_path, mode='r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:
                chars_stat[char] += 1

    return chars_stat.most_common()[-1][0]


def count_punctuation_chars(file_path: str) -> int:
    number_of_punctuation_chars = 0

    with open(file_path, mode='r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:

                if char in string.punctuation:
                    number_of_punctuation_chars += 1

    return number_of_punctuation_chars


def count_non_ascii_chars(file_path: str) -> int:
    number_of_non_ascii_chars = 0

    with open(file_path, mode='r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:

                if ord(char) > 127:
                    number_of_non_ascii_chars += 1

    return number_of_non_ascii_chars


def get_most_common_non_ascii_char(file_path: str) -> str:
    non_ascii_chars_stat = Counter()

    with open(file_path, mode='r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:

                if ord(char) > 127:
                    non_ascii_chars_stat[char] += 1

    return non_ascii_chars_stat.most_common()[0][0]
