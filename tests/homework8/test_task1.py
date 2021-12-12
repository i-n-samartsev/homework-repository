import os
from tempfile import NamedTemporaryFile

from pytest import fixture, raises

from homework8.task1 import KeyValueStorage


@fixture
def key_value_storage():
    try:
        with NamedTemporaryFile(mode='w', encoding='utf8',
                                delete=False) as file:
            file.write('name=kek\n')
            file.write('last_name=top\n')
            file.write('power=9001\n')
            file.write('song=shadilay\n')
        yield file.name
    finally:
        os.remove(file.name)


@fixture
def invalid_key_value_storage():
    try:
        with NamedTemporaryFile(mode='w', encoding='utf8',
                                delete=False) as file:
            file.write('1=something\n')
        yield file.name
    finally:
        os.remove(file.name)


def test_key_value_storage_get_attribute(key_value_storage):
    storage = KeyValueStorage(key_value_storage)
    assert storage.power == 9001
    assert storage.song == 'shadilay'


def test_key_value_storage_get_item(key_value_storage):
    storage = KeyValueStorage(key_value_storage)
    assert storage['power'] == 9001
    assert storage['song'] == 'shadilay'


def test_key_value_storage_get_non_existent_attr_raises_err(key_value_storage):
    storage = KeyValueStorage(key_value_storage)
    with raises(AttributeError):
        storage.non_exist


def test_key_value_storage_get_non_existent_item_raises_err(key_value_storage):
    storage = KeyValueStorage(key_value_storage)
    with raises(KeyError):
        storage['non_exist']


def test_key_value_storage_get_built_in_attribute(key_value_storage):
    storage = KeyValueStorage(key_value_storage)
    storage.__doc__ = 'Wrong doc'
    assert 'Wrapper class' in storage.__doc__


def test_key_value_storage_with_invalid_key_exc(invalid_key_value_storage):
    with raises(ValueError, match='invalid identifier'):
        KeyValueStorage(invalid_key_value_storage)
