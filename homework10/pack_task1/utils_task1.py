# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def float_normalizer(value_in_str):
    if "," in value_in_str:
        lst_repr = value_in_str.strip("%").split(",")
        return float("".join(lst_repr))

    return float(value_in_str.strip("%"))


if __name__ == "__main__":
    soup = BeautifulSoup(requests.get("https://markets.businessinsider.com/stocks/mmm-stock").text, "lxml")
