"""
Write a function that takes directory path, a file extension and an optional
tokenizer. It will count lines in all files with that extension if there are
no tokenizer. If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, 'txt')
# 6
# >>> universal_file_counter(test_dir, 'txt', str.split)
# 6

"""
import os
from pathlib import Path
from typing import Callable, Optional, Union


def get_tokens_from_file(file, tokenizer: Optional[Callable] = None) -> int:
    with open(file, mode='r') as file:
        counter = 0
        if tokenizer:
            for line in file:
                counter += len(tokenizer(line))
        else:
            for _ in file:
                counter += 1
        return counter


def universal_file_counter(dir_path: Union[Path, str],
                           file_ext: str,
                           tokenizer: Optional[Callable] = None) -> int:
    counter = 0

    for dirname, folders, files in os.walk(dir_path):

        for folder in folders:
            folder = os.path.join(dirname, folder)
            counter += universal_file_counter(folder, file_ext, tokenizer)

        for file in files:
            file = os.path.join(dirname, file)
            base, ext = os.path.splitext(file)
            if ext[1:] != file_ext:
                continue
            counter += get_tokens_from_file(file, tokenizer)

    return counter


if __name__ == '__main__':
    TEST_DIR = os.getcwd()
    print(universal_file_counter(TEST_DIR, 'txt'))  # 6

    print(universal_file_counter(TEST_DIR, 'txt', str.split))   # 6
