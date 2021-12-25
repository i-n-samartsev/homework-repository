"""
Write a function that takes directory path, a file extension and an optional
tokenizer. It will count lines in all files with that extension if there are
no tokenizer. If tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(os.path.dirname(__file__), '.txt')
6
>>> universal_file_counter(os.path.dirname(__file__), '.txt', str.split)
6

"""
import os
from pathlib import Path
from typing import Callable, Optional, Union


def get_tokens_from_file(file: Union[Path, str],
                         tokenizer: Optional[Callable] = None) -> int:
    """
        Function that takes file path and an optional tokenizer. Count lines
        in that file if there are no tokenizer. If tokenizer is not None, it
        will count tokens.
    """
    with open(file, mode='r') as file:
        if tokenizer:
            counter = sum(len(tokenizer(line)) for line in file)
        else:
            counter = sum(1 for line in file)
        return counter


def universal_file_counter(dir_path: Union[Path, str],
                           file_ext: str,
                           tokenizer: Optional[Callable] = None) -> int:
    """
        Function that takes directory path, a file extension and an optional
        tokenizer. Count lines in all files with that extension if there are
        no tokenizer. If tokenizer is not None, it will count tokens.
        Extension form: '.ext'
    """
    counter = 0

    for dirname, folders, files in os.walk(dir_path):
        for file in files:
            base, ext = os.path.splitext(file)
            full_file_path = os.path.join(dirname, file)
            if ext != file_ext:
                continue
            counter += get_tokens_from_file(full_file_path, tokenizer)
    return counter
