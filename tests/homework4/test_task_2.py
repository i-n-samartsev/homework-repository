from unittest.mock import patch

import pytest

from homework4.task_2_mock_input import (DotsOnIError, NetworkClient,
                                         count_dots_on_i)


class FakeNetworkClient:
    """
        Fake small service class for simple network requests
    """
    def __init__(self, url):
        self.url = url

    @property
    def html(self) -> str:
        return self.url


def test_count_dots_on_i_return_correct_answer():
    assert count_dots_on_i('https://example.com/') == 59


def test_count_dots_on_i_raise_exception_on_wrong_url():
    with pytest.raises(DotsOnIError):
        count_dots_on_i('https://abacab.abacab/')


def test_count_dots_on_i_with_patch_object_return_correct_answer():
    with patch.object(NetworkClient, 'html', FakeNetworkClient.html):
        assert count_dots_on_i('https://github.com/zhuchkov-artem') == 1


def test_count_dots_on_i_with_patch_return_correct_answer():
    with patch('homework4.task_2_mock_input.NetworkClient',
               new=FakeNetworkClient):
        assert count_dots_on_i('https://github.com/zhuchkov-artem') == 1


def test_count_dots_on_i_with_patch_raise_exception_on_correct_url():
    with patch('homework4.task_2_mock_input.NetworkClient',
               side_effect=DotsOnIError):
        with pytest.raises(DotsOnIError):
            count_dots_on_i('https://example.com/')
