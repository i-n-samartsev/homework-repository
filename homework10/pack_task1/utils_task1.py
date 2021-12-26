# -*- coding: utf-8 -*-

import asyncio
import ssl

import aiohttp
import requests
from bs4 import BeautifulSoup

url_list = [
    "https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530396000&before=1530436000",
    "https://api.pushshift.io/reddit/search/comment/?q=Nestle&size=30&after=1530436000&before=1530476000",
]


async def fetch(session, url):
    async with session.get(url, ssl=ssl.SSLContext()) as response:
        return await response.json()


async def fetch_all(urls, loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url) for url in urls], return_exceptions=True)
        return results


if __name__ == "__main__":
    page = requests.get("https://markets.businessinsider.com/index/components/s&p_500?p=1")

    soup = BeautifulSoup(page.text, "lxml")

    tds = soup.find("table", class_="table__layout--fixed").find_all("td", "table__td--big")
    pgs = soup.find("div", class_="finando_paging margin-top--small").find_all("a")
    pers = soup.find("table", class_="table__layout--fixed").find_all("tr")

    companies = []
    comp_links = []
    persentages = []
    pages = []
    pages_links = []

    for td in tds:
        companies.append(td.find("a").get("title"))
        comp_links.append(td.find("a").get("href"))

    for page in pgs:
        pages_links.append(page.get("href"))

    # table_columns = soup.find_all("tr")[0].find_all("th")
    #
    # for tr in soup.find_all("tr")[1:]:
    #     tds = tr.find_all("td")
    #     vals = [tds[0].text.strip(), tds[1].text.strip(), tds[2].text.strip()]
    #     print(tds[0].text, "  ", tds[1].text, "  ", tds[2].text)

    print()
