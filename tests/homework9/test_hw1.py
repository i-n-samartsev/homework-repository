import os
from tempfile import NamedTemporaryFile

from pytest import fixture, raises

from homework9.hw1 import merge_sorted_files


@fixture
def equal_length_files():
    texts = equal_length_texts()
    filenames = []
    for text in texts:
        with NamedTemporaryFile(mode='w', delete=False) as file:
            file.write(text)
        filenames.append(file.name)
    try:
        yield filenames
    finally:
        for filename in filenames:
            os.remove(filename)


@fixture
def diff_length_files():
    texts = diff_length_texts()
    filenames = []
    for text in texts:
        with NamedTemporaryFile(mode='w', delete=False) as file:
            file.write(text)
        filenames.append(file.name)
    try:
        yield filenames
    finally:
        for filename in filenames:
            os.remove(filename)


@fixture
def empty_files():
    texts = empty_texts()
    filenames = []
    for text in texts:
        with NamedTemporaryFile(mode='w', delete=False) as file:
            file.write(text)
        filenames.append(file.name)
    try:
        yield filenames
    finally:
        for filename in filenames:
            os.remove(filename)


@fixture
def files_with_non_integers():
    texts = texts_with_non_integers()
    filenames = []
    for text in texts:
        with NamedTemporaryFile(mode='w', delete=False) as file:
            file.write(text)
        filenames.append(file.name)
    try:
        yield filenames
    finally:
        for filename in filenames:
            os.remove(filename)


def equal_length_texts():
    text1 = '\n'.join(['-4', '-1', '2'])
    text2 = '\n'.join(['-3', '0', '3'])
    text3 = '\n'.join(['-2', '1', '4'])
    return [text1, text2, text3]


def diff_length_texts():
    text1 = '-4'
    text2 = '\n'.join(['-3', '-1', '1'])
    text3 = '\n'.join(['-2', '0', '2', '3', '4'])
    return [text1, text2, text3]


def empty_texts():
    return ['', '', '']


def texts_with_non_integers():
    text1 = '\n'.join(['0', '2', '4'])
    text2 = '\n'.join(['1', 'fizz', 'buzz'])
    return [text1, text2]


def test_merge_sorted_equal_length_files(equal_length_files):
    assert list(merge_sorted_files(equal_length_files)) == list(range(-4, 5))


def test_merge_sorted_different_length_files(diff_length_files):
    assert list(merge_sorted_files(diff_length_files)) == list(range(-4, 5))


def test_merge_sorted_empty_files(empty_files):
    assert list(merge_sorted_files(empty_files)) == []


def test_merge_sorted_non_integers_files_raises_error(files_with_non_integers):
    with raises(ValueError, match='is not an integer'):
        list(merge_sorted_files(files_with_non_integers))
