import os

import pytest

from homework4.task_1_read_file import read_magic_number


@pytest.fixture()
def create_and_del_true_file():
    with open(file='test_file.txt', mode='w', encoding='utf8') as file:
        file.write('1')
    yield
    os.remove('test_file.txt')


@pytest.fixture()
def create_and_del_false_file():
    with open(file='test_file.txt', mode='w', encoding='utf8') as file:
        file.write('3')
    yield
    os.remove('test_file.txt')


@pytest.fixture()
def create_and_del_exception_file():
    with open(file='test_file.txt', mode='w', encoding='utf8') as file:
        file.write('abacab')
    yield
    os.remove('test_file.txt')


def test_read_magic_number_return_true(create_and_del_true_file):
    assert read_magic_number('test_file.txt') is True


def test_read_magic_number_return_false(create_and_del_false_file):
    assert read_magic_number('test_file.txt') is False


def test_read_magic_number_return_exception(create_and_del_exception_file):
    with pytest.raises(ValueError):
        read_magic_number('test_file.txt')


def test_read_magic_number_return_invalid_path(create_and_del_false_file):
    with pytest.raises(ValueError) as exc:
        read_magic_number('non-existent file.txt')
    assert 'Invalid path' in str(exc.value)
