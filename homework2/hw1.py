"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
from collections import Counter, defaultdict
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    words_stat = defaultdict(list)

    with open(file_path, mode='r', encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            words = line.split()
            for word in words:
                words_stat[len(word)].append(word.strip(string.punctuation))

    sorted_length = sorted(words_stat, reverse=True)
    answer = []

    for length in sorted_length:
        if not words_stat[length]:
            continue
        answer.append(words_stat[length].pop())
        if len(answer) > 9:
            break

    return answer


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
