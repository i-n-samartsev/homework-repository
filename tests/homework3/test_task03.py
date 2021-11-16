from homework3.task03 import make_filter
from homework3.task03 import sample_data


def test_make_filter_return_first_entry():
    kwargs = {'name': 'Bill', 'type': 'person'}
    assert make_filter(**kwargs).apply(sample_data) == [sample_data[0]]


def test_make_filter_return_second_entry():
    kwargs = {'name': 'polly', 'type': 'bird'}
    assert make_filter(**kwargs).apply(sample_data) == [sample_data[1]]


def test_make_filter_return_nothing():
    kwargs = {'name': 'polly', 'type': 'person'}
    assert make_filter(**kwargs).apply(sample_data) == []
