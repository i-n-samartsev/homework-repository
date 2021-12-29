# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def float_normalizer(value_in_str):
    if "," in value_in_str:
        lst_repr = value_in_str.strip("%").split(",")
        return float("".join(lst_repr))

    return float(value_in_str.strip("%"))


def get_base_response_text(url="https://markets.businessinsider.com/index/components/s&p_500"):
    """Returns response text data of base web-page needed for s&p500 list page counting"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text


def get_page_count(response_text, fixed_page_count=None):
    """Returns s&p500 list pages count"""
    if fixed_page_count:
        return fixed_page_count

    soup = BeautifulSoup(response_text, "lxml")
    div_class = "finando_paging margin-top--small"
    page_count = soup.find("div", class_=div_class).contents[19].contents[0]

    return int(page_count)


def get_page_links(page_count=1, base_link="https://markets.businessinsider.com/index/components/s&p_500?p="):
    return [base_link + str(num) for num in range(1, page_count + 1)]


if __name__ == "__main__":
    pass
