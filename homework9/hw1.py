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
from itertools import zip_longest
from pathlib import Path
from typing import Iterator, List, Union


class NotAnIntegerError(ValueError):
    """Exception class if file contains not only integers"""


def get_integers_from_file(filename: str) -> Iterator:
    with open(filename, mode='r') as file:
        for line_number, integer in enumerate(file, 1):
            try:
                yield int(integer.strip())
            except ValueError as err:
                raise NotAnIntegerError(f'{filename=} {line_number=} is not '
                                        f'an integer') from err


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    file_generators = map(get_integers_from_file, file_list)
    sentinel = object()
    for integers_pack in zip_longest(*file_generators, fillvalue=sentinel):
        integers_pack = filter(lambda x: x is not sentinel, integers_pack)
        for integer in integers_pack:
            yield integer
