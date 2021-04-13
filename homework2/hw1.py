"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import namedtuple  # ooops, i use it because it was on lecture
from string import ascii_lowercase, digits, printable, punctuation, whitespace
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """This function find 10 longest words consisting from largest
    amount of unique symbols"""
    with open(file_path) as fin:
        text = set(fin.read().split())

    UniqWord = namedtuple("UniqWord", ["count_uniq", "word"])
    top_ten_words = [UniqWord(0, "") for _ in range(10)]
    the_shortest_word_in_top_ten = 0

    for word in text:
        if len(set(word)) > the_shortest_word_in_top_ten:
            for index, word_from_top_ten in enumerate(top_ten_words):
                if word_from_top_ten.count_uniq < len(set(word)):
                    top_ten_words[index] = UniqWord(len(set(word)), word)
                    the_shortest_word_in_top_ten = min(
                        top_ten_words, key=lambda elem: elem.count_uniq
                    ).count_uniq
                    break
    return [elem.word for elem in top_ten_words]


def get_rarest_char(file_path: str) -> str:
    """This function find rarest symbol for document"""
    with open(file_path) as fin:
        text = fin.read().lower()

    char_counter = {}  # 'char': 'count'
    for char in text:
        if char not in whitespace + punctuation + digits:
            char_counter.setdefault(char, 0)
            char_counter[char] += 1
    try:
        return min(char_counter, key=lambda x: char_counter[x])
    except ValueError:
        return ""


def _count_symbols(file_path: str, symbols: str) -> int:
    """This function count every "symbols" char"""
    with open(file_path) as fin:
        text = fin.read()
    counter = 0
    for char in text:
        if char in symbols:
            counter += 1
    return counter


def count_punctuation_chars(file_path: str) -> int:
    """This function count every punctuation char"""
    return _count_symbols(file_path, punctuation)


def count_non_ascii_chars(file_path: str) -> int:
    """This function count every non ascii char"""
    return _count_symbols(file_path, ascii_lowercase)


def get_most_common_non_ascii_char(file_path: str) -> str:
    """ This function find most common non ascii char for document"""
    with open(file_path) as fin:
        text = fin.read().lower()
    non_ascii_chars = {}  # structure: char: counter
    for char in text:
        if char not in printable:
            non_ascii_chars.setdefault(char, 0)
            non_ascii_chars[char] += 1
    try:
        return max(non_ascii_chars.items(), key=lambda elem: elem[1])
    except ValueError:
        return ""
