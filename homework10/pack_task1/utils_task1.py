# -*- coding: utf-8 -*-

import asyncio
import re
import ssl

import aiohttp
import requests
from bs4 import BeautifulSoup

url_list = [
    "https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530396000&before=1530436000",
    "https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530436000&before=1530476000",
]


all_data = []


async def fetch(session, url):
    async with session.get(url, ssl=ssl.SSLContext()) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results


def float_normalizer(value_in_str):
    if "," in value_in_str:
        lst_repr = value_in_str.strip("%").split(",")
        return float("".join(lst_repr))

    return float(value_in_str.strip("%"))


async def get_page_data(session, category: str, page_id: int) -> str:
    if page_id:
        url = f"https://ozon.ru/brand/{category}/?page={page_id}"
    else:
        url = f"https://ozon.ru/brand/{category}/"
    async with session.get(url) as resp:
        assert resp.status == 200
        print(f"get url: {url}")
        resp_text = await resp.text()
        all_data.append(resp_text)
        return resp_text


async def load_site_data():
    categories_list = ["playstation-79966341", "adidas-144082850", "bosch-7577796", "lego-19159896"]
    async with aiohttp.ClientSession() as session:
        tasks = []
        for cat in categories_list:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(session, cat, page_id))
                tasks.append(task)
                # process text and do whatever we need...
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    # asyncio.run(load_site_data())
    # soup = BeautifulSoup(requests.get("https://markets.businessinsider.com/stocks/mmm-stock").text, "lxml")
    tag_class_name_low = "snapshot__data-item snapshot__data-item--small"
    tag_class_name_high = "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"

    soup = BeautifulSoup(requests.get("https://markets.businessinsider.com/stocks/uaa-stock").text, "lxml")

    code = soup.find("span", class_="price-section__category").find("span").contents[0].strip()
    name = soup.find("span", class_="price-section__label").contents[0]
    p_e = float(soup.find("div", text=re.compile("P/E Ratio")).parent.text.strip().strip("P/E Ratio").strip())

    week_52_low = float_normalizer(soup.find("div", class_=tag_class_name_low).contents[0].strip())
    week_52_high = float_normalizer(soup.find("div", class_=tag_class_name_high).contents[0].strip())
    week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)

    name = soup.find("div", class_="price-section__row")
    print()
