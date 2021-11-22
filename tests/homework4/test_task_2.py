from unittest.mock import patch

import pytest

from homework4.task_2_mock_input import count_dots_on_i


def test_count_dots_on_i_return_correct_answer():
    assert count_dots_on_i('https://example.com/') == 59


def test_count_dots_on_i_raise_exception_on_wrong_url():
    with pytest.raises(ValueError):
        count_dots_on_i('https://abacab.abacab/')


def test_count_dots_on_i_with_mock_return_correct_answer():
    path_for_mock = 'homework4.task_2_mock_input.get_html_from_url'
    with patch(target=path_for_mock, return_value='iii'):
        assert count_dots_on_i('https://example.com/') == 3


def test_count_dots_on_i_with_mock_raise_exception_on_correct_url():
    path_for_mock = 'homework4.task_2_mock_input.get_html_from_url'
    with patch(target=path_for_mock, side_effect=ValueError):
        with pytest.raises(ValueError):
            count_dots_on_i('https://example.com/')
