"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(['file1.txt', 'file2.txt']))
[1, 2, 3, 4, 5, 6]
"""
from heapq import merge
from pathlib import Path
from typing import Iterator, List, Union


class NotAnIntegerError(ValueError):
    """Exception class if file contains not only integers"""
    def __init__(self, message=''):
        self.message = message

    def __str__(self):
        return f'{self.message} is not an integer'


def get_integers_from_file(filename: str) -> Iterator:
    with open(filename, mode='r') as file:
        for line_number, integer in enumerate(file, 1):
            try:
                yield int(integer.strip())
            except ValueError:
                raise NotAnIntegerError(f'{filename=} {line_number=}')


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    file_iterators = map(get_integers_from_file, file_list)
    iter_row = {}
    for iterator in file_iterators:
        value = next(iterator, None)
        if value is not None:
            iter_row[iterator] = value
    while iter_row:
        next_iterator = min(iter_row, key=iter_row.get)
        yield iter_row[next_iterator]
        value = next(next_iterator, None)
        if value is not None:
            iter_row[next_iterator] = value
        else:
            iter_row.pop(next_iterator)

# Another solution with heapq.merge


def merge_sorted_files_with_heapq(file_list) -> Iterator:
    file_iterators = map(get_integers_from_file, file_list)
    yield from merge(*file_iterators)
