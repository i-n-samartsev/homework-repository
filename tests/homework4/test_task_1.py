import os
from tempfile import NamedTemporaryFile

import pytest

from homework4.task_1_read_file import (FileDoesNotExist, FileIsEmpty,
                                        MagicNumberError, read_magic_number)


@pytest.fixture
def file_with_1_in_first_line():
    try:
        with NamedTemporaryFile(mode='w', encoding='utf8',
                                delete=False) as file:
            file.write('1')
        yield file.name
    finally:
        os.remove(file.name)


@pytest.fixture()
def file_with_3_in_first_line():
    try:
        with NamedTemporaryFile(mode='w', encoding='utf8',
                                delete=False) as file:
            file.write('3')
        yield file.name
    finally:
        os.remove(file.name)


@pytest.fixture()
def file_with_abacab_in_first_line():
    try:
        with NamedTemporaryFile(mode='w', encoding='utf8',
                                delete=False) as file:
            file.write('abacab')
        yield file.name
    finally:
        os.remove(file.name)


@pytest.fixture()
def empty_file():
    try:
        with NamedTemporaryFile(mode='w', encoding='utf8',
                                delete=False) as file:
            pass
        yield file.name
    finally:
        os.remove(file.name)


def test_read_magic_number_return_true(file_with_1_in_first_line):
    assert read_magic_number(file_with_1_in_first_line) is True


def test_read_magic_number_return_false(file_with_3_in_first_line):
    assert read_magic_number(file_with_3_in_first_line) is False


def test_read_magic_number_return_magic_error(file_with_abacab_in_first_line):
    with pytest.raises(MagicNumberError):
        read_magic_number(file_with_abacab_in_first_line)


def test_read_magic_number_return_invalid_path_exception():
    with pytest.raises(FileDoesNotExist):
        read_magic_number('non-existent file.txt')


def test_read_magic_number_return_file_is_empty_exception(empty_file):
    with pytest.raises(FileIsEmpty):
        read_magic_number(empty_file)
