# -*- coding: utf-8 -*-

from ..pack_task1.module_task1 import CorpDataParser


def test_pos_build_data_table(html_3m_details_text_data, growth_table):
    """Checks if computing and building is alive"""
    data_table = CorpDataParser([html_3m_details_text_data], growth_table)
    data_table.compute_data()
    data_table.build_data_table()


def test_pos_generate_top(html_3m_details_text_data, growth_table, data_table_fixture):
    """Checks if report is being build and not empty"""
    data_table = CorpDataParser([html_3m_details_text_data], growth_table)
    data_table.compute_data()
    data_table.build_data_table()
    lst = data_table.generate_top("price", length=1)

    assert lst == data_table_fixture
