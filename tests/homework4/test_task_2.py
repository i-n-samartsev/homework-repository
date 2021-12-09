from unittest.mock import patch
from urllib.error import URLError

import pytest

import homework4.task_2_mock_input
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


def test_count_dots_on_i_with_patching_client_method_return_correct_answer():
    with patch.object(NetworkClient,
                      'html',
                      FakeNetworkClient.html):
        assert count_dots_on_i('https://github.com/zhuchkov-artem') == 1


def test_count_dots_on_i_with_patching_full_client_return_correct_answer():
    with patch.object(homework4.task_2_mock_input,
                      'NetworkClient',
                      FakeNetworkClient):
        assert count_dots_on_i('https://github.com/zhuchkov-artem') == 1


def test_count_dots_on_i_with_patch_urlopen_raise_exception():
    with patch.object(homework4.task_2_mock_input, 'urlopen',
                      side_effect=URLError('Incorrect URL')):
        with pytest.raises(DotsOnIError):
            count_dots_on_i('https://example.com/')
