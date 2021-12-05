import os

import pytest

from homework4.task_1_read_file import (FileDoesNotExist, FileIsEmpty,
                                        MagicNumberError, read_magic_number)


@pytest.fixture()
def file_with_1_in_first_line():
    with open(file='test_file.txt', mode='w', encoding='utf8') as file:
        file.write('1')
    yield
    os.remove('test_file.txt')


@pytest.fixture()
def file_with_3_in_first_line():
    with open(file='test_file.txt', mode='w', encoding='utf8') as file:
        file.write('3')
    yield
    os.remove('test_file.txt')


@pytest.fixture()
def file_with_abacab_in_first_line():
    with open(file='test_file.txt', mode='w', encoding='utf8') as file:
        file.write('abacab')
    yield
    os.remove('test_file.txt')


@pytest.fixture()
def empty_file():
    with open(file='test_file.txt', mode='w', encoding='utf8'):
        pass
    yield
    os.remove('test_file.txt')


def test_read_magic_number_return_true(file_with_1_in_first_line):
    assert read_magic_number('test_file.txt') is True


def test_read_magic_number_return_false(file_with_3_in_first_line):
    assert read_magic_number('test_file.txt') is False


def test_read_magic_number_return_magic_error(file_with_abacab_in_first_line):
    with pytest.raises(MagicNumberError):
        read_magic_number('test_file.txt')


def test_read_magic_number_return_invalid_path_exception():
    with pytest.raises(FileDoesNotExist):
        read_magic_number('non-existent file.txt')


def test_read_magic_number_return_file_is_empty_exception(empty_file):
    with pytest.raises(FileIsEmpty):
        read_magic_number('test_file.txt')
