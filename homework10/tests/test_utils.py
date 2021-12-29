# -*- coding: utf-8 -*-


from homework10.pack_task1.parse_utils import (
    corp_code_parse,
    corp_max_profit_parse,
    corp_name_parse,
    corp_pe_parse,
    corp_price_parse,
    urls_growth_parse,
)

from ..pack_task1.connection_utils import (
    float_normalizer,
    get_page_count,
    get_page_links,
)


def test_pos_float_normaliser():
    assert float_normalizer("1,200.1") == 1200.1


def test_pos_get_page_count(html_base_response_text_data):
    assert get_page_count(html_base_response_text_data, fixed_page_count=None) == 11


def test_pos_get_page_count_fixed_page_count(html_base_response_text_data):
    assert get_page_count(html_base_response_text_data, fixed_page_count=1) == 1


def test_pos_get_links(html_base_response_text_data):
    assert len(get_page_links()) == 1


def test_pos_urls_growth_parse(html_base_response_text_data):
    assert len(urls_growth_parse(html_base_response_text_data)) == 50


def test_pos_corp_name_parse(html_3m_details_text_data):
    assert corp_name_parse(html_3m_details_text_data) == "3M Co. "


def test_pos_corp_code_parse(html_3m_details_text_data):
    assert corp_code_parse(html_3m_details_text_data) == "MMM"


def test_pos_corp_price_parse(html_3m_details_text_data):
    assert corp_price_parse(html_3m_details_text_data, 73.6514) == 13082.7


def test_pos_corp_pe_parse(html_3m_details_text_data):
    assert corp_pe_parse(html_3m_details_text_data) == 19.91


def test_pos_corp_max_profit_parse(html_3m_details_text_data):
    assert corp_max_profit_parse(html_3m_details_text_data) == 27.85
