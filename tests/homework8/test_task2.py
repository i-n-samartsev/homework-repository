import os
import sqlite3
from contextlib import contextmanager

from pytest import fixture, raises

from homework8.task2 import TableData

DATABASE = os.path.join(os.path.dirname(__file__), 'example.sqlite')


@fixture
def presidents():
    presidents = TableData(database_name=DATABASE, table_name='presidents')
    try:
        yield presidents
    finally:
        presidents.close_con_to_bd()


@contextmanager
def add_new_president():
    con2 = sqlite3.connect(DATABASE)
    cursor2 = con2.cursor()
    cursor2.execute("INSERT INTO presidents VALUES ('Lincoln', 52, 'USA')")
    con2.commit()
    cursor2.close()
    con2.close()
    try:
        yield 'Lincoln', 52, 'USA'
    finally:
        con2 = sqlite3.connect(DATABASE)
        cursor2 = con2.cursor()
        cursor2.execute("DELETE FROM presidents WHERE name=='Lincoln'")
        con2.commit()
        cursor2.close()
        con2.close()


def test_table_data_length(presidents):
    assert len(presidents) == 3


def test_table_data_get_item(presidents):
    assert presidents['Trump'] == ('Trump', 1337, 'US')


def test_table_data_get_non_existent_item(presidents):
    with raises(KeyError):
        presidents['Putin']


def test_table_data_contains_return_true(presidents):
    assert ('Trump' in presidents) is True


def test_table_data_contains_return_false(presidents):
    assert ('Putin' in presidents) is False


def test_table_data_iteration(presidents):
    ages = []
    for president in presidents:
        ages.append(president['age'])

    assert ages == [999, 1337, 101]


def test_table_data_reflect_most_recent_data(presidents):
    assert len(presidents) == 3
    with add_new_president() as new_president:
        assert len(presidents) == 4
        assert presidents['Lincoln'] == new_president
    assert len(presidents) == 3
