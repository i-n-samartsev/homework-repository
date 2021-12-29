# -*- coding: utf-8 -*-

import re

from bs4 import BeautifulSoup, SoupStrainer

from .connection_utils import float_normalizer


def urls_growth_parse(text_data):
    base_url = "https://markets.businessinsider.com"
    limiter = SoupStrainer("table")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    url_cells = soup.find("table", class_="table__layout--fixed").find_all("td", "table__td--big")
    table_rows = soup.find("table", class_="table__layout--fixed").find_all("tr")[1:]  # skip table header

    urls = []
    growth_percentages = []

    for cell in url_cells:
        urls.append(base_url + cell.find("a").get("href"))

    for row in table_rows:
        percentage_cell = row.find_all("td")[7]
        cell_value = percentage_cell.find_all("span")[1]
        growth_percentages.append(float_normalizer(cell_value.contents[0]))

    parsed_data = []

    for url, percentage in zip(urls, growth_percentages):
        parsed_data.append({"url": url, "year_growth": percentage})

    return parsed_data


def corp_name_parse(text_data):
    limiter = SoupStrainer("span")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    print("parsed some name")
    return soup.find("span", class_="price-section__label").contents[0]


def corp_code_parse(text_data):
    limiter = SoupStrainer("span")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    print("parsed some code")

    return soup.find("span", class_="price-section__category").find("span").contents[0].strip(",").strip(" ")


def corp_price_parse(text_data, rub_rate):
    limiter = SoupStrainer("div")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)

    try:
        price = float_normalizer(
            soup.find("div", text=re.compile("Prev. Close")).parent.text.strip().strip("Prev. Close").strip()
        )
        price = round(rub_rate * price, 2)
    except AttributeError:
        price = None

    print("parsed some price")
    return price


def corp_pe_parse(text_data):
    limiter = SoupStrainer("div")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)

    try:
        p_e = float_normalizer(
            soup.find("div", text=re.compile("P/E Ratio")).parent.text.strip().strip("P/E Ratio").strip()
        )
    except AttributeError:
        p_e = None

    print("parsed some PE")
    return p_e


def corp_max_profit_parse(text_data):
    limiter = SoupStrainer("div")
    soup = BeautifulSoup(text_data, "lxml", parse_only=limiter)
    tag_class_name_low = "snapshot__data-item snapshot__data-item--small"
    tag_class_name_high = "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"

    try:
        week_52_low = float_normalizer(soup.find_all("div", class_=tag_class_name_low)[1].contents[0].strip())
        week_52_high = float_normalizer(soup.find_all("div", class_=tag_class_name_high)[1].contents[0].strip())
        week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)
    except IndexError:
        try:
            week_52_low = float_normalizer(soup.find_all("div", class_=tag_class_name_low)[0].contents[0].strip())
            week_52_high = float_normalizer(soup.find_all("div", class_=tag_class_name_high)[0].contents[0].strip())
            week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)
        except IndexError:
            week_profit = None

    print("parsed some profits")
    return week_profit


if __name__ == "__main__":
    pass
