"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from functools import partial
from typing import Generator, List
from unicodedata import category


def get_file_text(filename: str, encoding: str = 'utf8',
                  errors: str = 'strict',
                  chunk_size: int = 64) -> Generator:
    """
    Generator that iterates over the file by chunks.
    """
    with open(filename, mode='r', encoding=encoding, errors=errors) as file:
        for chunk in iter(partial(file.read, chunk_size), ''):
            yield chunk


def get_word(file_path: str, encoding: str = 'utf8',
             errors: str = 'strict') -> Generator:
    """
    Generator that yields only words from file.
    """
    buffer = ''
    for symbol in get_file_text(file_path, encoding=encoding, errors=errors,
                                chunk_size=1):
        if category(symbol).startswith('L'):
            buffer += symbol
        else:
            if buffer:
                yield buffer
                buffer = ''


def get_longest_diverse_words(file_path: str, encoding: str = 'utf8',
                              errors: str = 'strict',
                              quantity: int = 10) -> List[str]:
    """
    Returns longest diverse word list of the file.
    """
    words_stat = {}

    for word in get_word(file_path, encoding=encoding, errors=errors):
        words_stat[len(word)] = words_stat.get(len(word), []) + [word]

    sorted_length = sorted(words_stat, reverse=True)
    longest_words = []

    for length in sorted_length:
        while len(longest_words) < quantity and words_stat[length]:
            next_word = words_stat[length].pop()
            if next_word not in longest_words:
                longest_words.append(next_word)

    return longest_words


def get_rarest_char(file_path: str, encoding: str = 'utf8',
                    errors: str = 'strict') -> str:
    """
    Returns the rarest char of the file.
    """
    chars_stat = {}

    for symbol in get_file_text(file_path, encoding, errors, chunk_size=1):
        chars_stat[symbol] = chars_stat.get(symbol, 0) + 1

    rarest_char = sorted(chars_stat, key=chars_stat.get)[0]
    return rarest_char


def count_punctuation_chars(file_path: str, encoding: str = 'utf8',
                            errors: str = 'strict') -> int:
    """
    Returns quantity of punctuation chars of the file.
    """
    number_of_punctuation_chars = 0

    for symbol in get_file_text(file_path, encoding, errors, chunk_size=1):
        if category(symbol).startswith('P'):
            number_of_punctuation_chars += 1

    return number_of_punctuation_chars


def count_non_ascii_chars(file_path: str, encoding: str = 'utf8',
                          errors: str = 'strict') -> int:
    """
    Returns quantity of non ascii chars of the file.
    """
    number_of_non_ascii_chars = 0

    for symbol in get_file_text(file_path, encoding, errors, chunk_size=1):
        if not symbol.isascii():
            number_of_non_ascii_chars += 1

    return number_of_non_ascii_chars


def get_most_common_non_ascii_char(file_path: str, encoding: str = 'utf8',
                                   errors: str = 'strict') -> str:
    """
    Returns the most common non ascii char of the file.
    """
    non_ascii_stat = {}

    for symbol in get_file_text(file_path, encoding, errors, chunk_size=1):
        if not symbol.isascii():
            non_ascii_stat[symbol] = non_ascii_stat.get(symbol, 0) + 1

    most_common_non_ascii_char = sorted(non_ascii_stat,
                                        key=non_ascii_stat.get,
                                        reverse=True)[0]
    return most_common_non_ascii_char
