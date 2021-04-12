"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from collections import namedtuple  # ooops, i use it because it was on lecture
from string import whitespace, punctuation, digits


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path) as fin:
        text = set(fin.read().split())

    UniqWord = namedtuple('UniqWord', ['count_uniq', 'word'])
    top_ten_words = [UniqWord(0, '') for _ in range(10)]
    the_shortest_word_in_top_ten = 0

    for word in text:
        if len(set(word)) > the_shortest_word_in_top_ten:
            for index, word_from_top_ten in enumerate(top_ten_words):
                if word_from_top_ten.count_uniq < len(set(word)):
                    top_ten_words[index] = UniqWord(len(set(word)), word)
                    the_shortest_word_in_top_ten = \
                        min(top_ten_words, key=
                            lambda elem: elem.count_uniq).count_uniq
                    break
    return [elem.word for elem in top_ten_words]


def get_rarest_char(file_path: str) -> str:
    with open(file_path) as fin:
        text = fin.read().lower()

    char_counter = {}  # 'char': 'count'
    for char in text:
        if char not in whitespace + punctuation + digits:
            char_counter.setdefault(char, 0)
            char_counter[char] += 1
    return min(char_counter, key=lambda x: char_counter[x])


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
