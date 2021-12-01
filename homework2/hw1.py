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
from functools import partial
from typing import List, Any, Hashable
from unicodedata import category
from dataclasses import dataclass


@dataclass
class Token:
    kind: str
    value: str


def add_to_stat(key: Hashable, value: Any, stat: dict):
    if key in stat:
        stat[key] += value
    else:
        stat[key] = value


def get_file_text(filename: str, encoding: str = 'utf8',
                  errors: str = 'strict', chunk_size: int = 64):
    with open(filename, mode='r', encoding=encoding, errors=errors) as file:
        for chunk in iter(partial(file.read, chunk_size), ''):
            yield chunk


def tokenize(chunk):
    buffer = ''
    for symbol in chunk:
        if category(symbol).startswith('L'):
            buffer += symbol
        else:
            if buffer:
                yield Token(kind='word', value=buffer)
                buffer = ''
            yield Token(kind='symbol', value=symbol)


# def get_longest_diverse_words(file_path: str, encoding: str = 'utf8',
#                               errors: str = 'strict') -> List[str]:
#     words_stat = {}
#
#     with open(file_path, mode='r', encoding='unicode-escape',
#               errors='ignore') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 words_stat[len(word)].append(word.strip(string.punctuation))
#
#     sorted_length = sorted(words_stat, reverse=True)
#     answer = []
#
#     for length in sorted_length:
#         if not words_stat[length]:
#             continue
#         answer.append(words_stat[length].pop())
#         if len(answer) > 9:
#             break
#
#     return answer


def get_rarest_char(file_path: str, encoding: str = 'utf8',
                    errors: str = 'strict') -> str:
    chars_stat = {}

    for chunk in get_file_text(file_path, encoding=encoding, errors=errors):
        for symbol in chunk:
            add_to_stat(key=symbol, value=1, stat=chars_stat)

    rarest_char = sorted(chars_stat, key=chars_stat.get)[0]
    return rarest_char


a = get_rarest_char('data.txt', encoding='unicode-escape', errors='ignore')
print(a)


def count_punctuation_chars(file_path: str, encoding: str = 'utf8',
                            errors: str = 'strict') -> int:
    number_of_punctuation_chars = 0

    for chunk in get_file_text(file_path, encoding=encoding, errors=errors):
        for symbol in chunk:
            if category(symbol).startswith('P'):
                number_of_punctuation_chars += 1

    return number_of_punctuation_chars


a = count_punctuation_chars('data.txt', encoding='unicode-escape',
                            errors='ignore')
print(a)


def count_non_ascii_chars(file_path: str, encoding: str = 'utf8',
                          errors: str = 'strict') -> int:
    number_of_non_ascii_chars = 0

    for chunk in get_file_text(file_path, encoding=encoding, errors=errors):
        for symbol in chunk:
            if not symbol.isascii():
                number_of_non_ascii_chars += 1

    return number_of_non_ascii_chars


a = count_non_ascii_chars('data.txt', encoding='unicode-escape',
                          errors='ignore')
print(a)


def get_most_common_non_ascii_char(file_path: str, encoding: str = 'utf8',
                                   errors: str = 'strict') -> str:
    non_ascii_chars_stat = {}

    for chunk in get_file_text(file_path, encoding=encoding, errors=errors):
        for symbol in chunk:
            if not symbol.isascii():
                add_to_stat(key=symbol, value=1, stat=non_ascii_chars_stat)

    most_common_non_ascii_char = sorted(non_ascii_chars_stat,
                                        key=non_ascii_chars_stat.get)[-1]
    return most_common_non_ascii_char


a = get_most_common_non_ascii_char('data.txt', encoding='unicode-escape',
                                   errors='ignore')
print(a)
