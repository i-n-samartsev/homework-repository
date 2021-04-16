"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from string import ascii_lowercase, digits, punctuation, whitespace
from typing import List


def read_ascii_file(file_path: str) -> str:
    r"""This function read text with \uXXXX symbols"""
    with open(file_path) as fin:
        text = fin.read()
    return bytes(text, 'ascii').decode('unicode-escape')


def get_longest_diverse_words(file_path: str) -> List[str]:
    """This function find 10 longest words consisting from largest
    amount of unique symbols"""
    text = set(read_ascii_file(file_path).split())
    top_ten_words = [(0, '') for _ in range(10)]
    the_shortest_word_in_top_ten = 0
    for word in text:
        if len(set(word)) > the_shortest_word_in_top_ten:
            for index, top_word in enumerate(top_ten_words):
                if top_word[0] < len(word):
                    top_ten_words[index] = (len(word), word)
                    the_shortest_word_in_top_ten = min(top_ten_words,
                                                       key=lambda l: l[0])[0]
                    break
    return [word[1] for word in top_ten_words]


def get_rarest_char(file_path: str) -> str:
    """This function find rarest symbol for document"""
    char_counter = {}  # 'char': 'count'
    for char in read_ascii_file(file_path).lower():
        if char not in whitespace + punctuation + digits + '‹›—«»':
            char_counter.setdefault(char, 0)
            char_counter[char] += 1
    try:
        return min(char_counter, key=lambda x: char_counter[x])
    except ValueError:
        return ""


def count_punctuation_chars(file_path: str) -> int:
    """This function count every punctuation char"""
    counter = 0
    for char in read_ascii_file(file_path):
        if char in punctuation + '‹›':
            counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    """This function count every non ascii char"""
    counter = 0
    for char in read_ascii_file(file_path).lower():
        if char not in ascii_lowercase + punctuation + digits + whitespace:
            counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    """ This function find most common non ascii char for document"""
    non_ascii_chars = {}  # structure: char: counter
    for char in read_ascii_file(file_path).lower():
        if char not in ascii_lowercase + punctuation + digits + whitespace:
            non_ascii_chars.setdefault(char, 0)
            non_ascii_chars[char] += 1
    try:
        return max(non_ascii_chars.items(), key=lambda elem: elem[1])
    except ValueError:
        return ""
