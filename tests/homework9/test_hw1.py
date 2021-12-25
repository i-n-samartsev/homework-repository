import os
from tempfile import NamedTemporaryFile

from pytest import fixture, raises

from homework9.hw1 import merge_sorted_files
from homework9.hw1 import merge_sorted_files_with_heapq as merge_with_heapq


@fixture
def file_creator():
    filenames = []

    def inner(texts):
        for text in texts:
            with NamedTemporaryFile(mode='w', delete=False) as file:
                file.write(text)
            filenames.append(file.name)
        return filenames

    try:
        yield inner
    finally:
        for filename in filenames:
            os.remove(filename)


def equal_length_texts():
    text1 = '\n'.join(['-4', '-2', '-1'])
    text2 = '\n'.join(['0', '2', '3'])
    text3 = '\n'.join(['-3', '1', '4'])
    return [text1, text2, text3]


def diff_length_texts():
    text1 = '-1'
    text2 = '\n'.join(['-3', '0', '1'])
    text3 = '\n'.join(['-4', '-2', '2', '3', '4'])
    return [text1, text2, text3]


def empty_texts():
    return ['', '', '']


def texts_with_non_integers():
    text1 = '\n'.join(['0', '2', '4'])
    text2 = '\n'.join(['1', 'fizz', 'buzz'])
    return [text1, text2]


def test_merge_sorted_equal_length_files(file_creator):
    equal_length_files = file_creator(equal_length_texts())
    assert list(merge_sorted_files(equal_length_files)) == list(range(-4, 5))
    assert list(merge_with_heapq(equal_length_files)) == list(range(-4, 5))


def test_merge_sorted_different_length_files(file_creator):
    diff_length_files = file_creator(diff_length_texts())
    assert list(merge_sorted_files(diff_length_files)) == list(range(-4, 5))
    assert list(merge_with_heapq(diff_length_files)) == list(range(-4, 5))


def test_merge_sorted_empty_files(file_creator):
    empty_files = file_creator(empty_texts())
    assert list(merge_sorted_files(empty_files)) == []
    assert list(merge_with_heapq(empty_files)) == []


def test_merge_sorted_non_integers_files_raises_error(file_creator):
    files_with_non_integers = file_creator(texts_with_non_integers())
    with raises(ValueError, match='is not an integer'):
        list(merge_sorted_files(files_with_non_integers))
    with raises(ValueError, match='is not an integer'):
        list(merge_with_heapq(files_with_non_integers))
