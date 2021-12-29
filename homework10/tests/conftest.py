# -*- coding: utf-8 -*-

import os

import pytest


@pytest.fixture()
def html_base_response_text_data():
    path_to_tests = os.getcwd()
    with open(path_to_tests + "/homework10/tests/test_data/base_response_text_data.txt") as src:
        data = src.read().replace("\n", "")
    return data


@pytest.fixture()
def html_3m_details_text_data():
    path_to_tests = os.getcwd()
    with open(path_to_tests + "/homework10/tests/test_data/3m_details_text_data.txt") as src:
        data = src.read().replace("\n", "")
    return data


@pytest.fixture()
def xml_rub_rate_text_data():
    path_to_tests = os.getcwd()
    with open(path_to_tests + "/homework10/tests/test_data/xml_rub_rate_text_data.txt") as src:
        data = src.read().replace("\n", "")
    return data


@pytest.fixture()
def growth_table():
    table = [0.17]
    return table


@pytest.fixture()
def data_table_fixture():
    table = [
        {"code": "MMM", "name": "3M Co. ", "price": 13082.7, "growth": 0.17, "PE": 19.91, "max_profit": 27.85},
    ]

    return table
