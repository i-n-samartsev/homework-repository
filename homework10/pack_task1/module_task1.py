"""
    Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
    https://markets.businessinsider.com/index/components/s&p_500

    Подробно про задание:
    https://github.com/lex-av/epam_python_autumn_2020/blob/main/lecture_10_parallelization/hw/stonks.md
"""


import asyncio
import re
import time
from multiprocessing.pool import ThreadPool

import aiohttp
import requests
import xmltodict
from bs4 import BeautifulSoup


class CorpoUrlsGetter:
    """
    Container to get and store corps pre-names, urls and year percent
    Implements list behavior (slices, len, getitem, iteration)
    Generates list of dicts with url and company growth percentage
    """

    def __init__(self, url="https://markets.businessinsider.com/index/components/s&p_500?p=", pages_count=11):
        self.domain = "https://markets.businessinsider.com"
        self.pages_count = pages_count
        self.pages_list = [url + str(page_number) for page_number in range(1, self.pages_count + 1)]
        self.corp_table = []
        self.table_links = []
        self.table_cursor = 0
        self.table_builder_threading()

    def __getitem__(self, index):
        if isinstance(index, slice):
            # Get the start, stop, and step from the slice
            return [self.corp_table[ii] for ii in range(*index.indices(len(self.corp_table)))]
        elif isinstance(index, int):
            if index < len(self.corp_table):
                return self.corp_table[index]
            else:
                raise IndexError("Index is out of range.")
        else:
            raise TypeError("Invalid argument type.")

    def __next__(self):
        if len(self.corp_table) > self.table_cursor:
            value = self.corp_table[self.table_cursor]
            self.table_cursor += 1
            return value
        else:
            raise StopIteration

    def __contains__(self, link):
        if link in self.table_links:
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.corp_table)

    @staticmethod
    def percentage_normalizer(value_in_str):
        """Converts given str from web-page to float"""
        if "," in value_in_str:
            lst_repr = value_in_str.strip("%").split(",")
            return float("".join(lst_repr))

        return float(value_in_str.strip("%"))

    def append_page_data(self, url):
        """Parse table on the page for urls and percentages"""
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        page_data = []
        link_cells = soup.find("table", class_="table__layout--fixed").find_all("td", "table__td--big")
        rows = soup.find("table", class_="table__layout--fixed").find_all("tr")[1:]  # skip table header

        links = []
        percentages = []

        for cell in link_cells:
            links.append(self.domain + cell.find("a").get("href"))
            self.table_links.append(self.domain + cell.find("a").get("href"))

        for row in rows:
            percentage_cell = row.find_all("td")[7]
            cell_value = percentage_cell.find_all("span")[1]
            percentage_value = self.percentage_normalizer(cell_value.contents[0])
            percentages.append(percentage_value)

        for link, percentage in zip(links, percentages):
            # page_data.append(Corp._make([link, percentage]))
            page_data.append({"link": link, "percentage": percentage})

        self.corp_table += page_data

    def table_builder_threading(self):
        with ThreadPool(self.pages_count) as t_pool:
            t_pool.map(self.append_page_data, self.pages_list)


class CompanyDataTableAsync:
    """
    Collection to store S&P-500 corps parameters
    Gets Urls/percentage table-object from CorpoUrlsGetter

    Every Corp in output table has parameters:
    code | name | growth | price | PE | max_profit
    """

    def __init__(self, table_src):
        self.src_data = table_src
        self.data_table = []
        self.rate = self._get_rate()
        asyncio.run(self._table_builder())

    @staticmethod
    def _float_normalizer(value_in_str):
        """Converts given str from web-page to float"""
        if "," in value_in_str:
            lst_repr = value_in_str.strip("%").split(",")
            return float("".join(lst_repr))
        return float(value_in_str.strip())

    def _get_rate(self):
        """Return valute rate for current date"""
        data = asyncio.run(self._get_req())
        rate_data = xmltodict.parse(data)
        usd = float(rate_data["ValCurs"]["Valute"][10]["Value"].replace(",", "."))
        return usd

    async def _get_req(self):
        """aiohttp getter for valute rate xml-data from bank api"""
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.cbr.ru/scripts/XML_daily.asp") as resp:
                response = await resp.text()
                return response

    def generate_top_ten(self, parameter, rev=True):
        """Generates top ten corps from data_table by given parameter"""
        return sorted(self.data_table, key=lambda row: row[parameter], reverse=rev)[:10]

    async def _get_corp_data(self, session, url, percentage, rate):
        """Generates corp data-dict by parsing corp web-page"""
        async with session.get(url) as response:
            if response.status != 200:
                self.data_table.append(
                    {"code": None, "name": None, "growth": -1, "price": -1, "PE": -1, "max_profit": -1}
                )
            else:
                await asyncio.sleep(0.2)
                response_text = await response.text()
                soup = BeautifulSoup(response_text, "lxml")

                code = (
                    soup.find("span", class_="price-section__category").find("span").contents[0].strip(",").strip(" ")
                )
                name = soup.find("span", class_="price-section__label").contents[0]
                print(name)  # For debug purpose

                try:
                    price = self._float_normalizer(
                        soup.find("div", text=re.compile("Open")).parent.text.strip().strip("Open").strip()
                    )
                    price = round(rate * price, 2)
                except AttributeError:
                    price = -1

                try:
                    p_e = self._float_normalizer(
                        soup.find("div", text=re.compile("P/E Ratio")).parent.text.strip().strip("P/E Ratio").strip()
                    )
                except AttributeError:
                    p_e = -1

                tag_class_name_low = "snapshot__data-item snapshot__data-item--small"
                tag_class_name_high = "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"

                try:
                    week_52_low = self._float_normalizer(
                        soup.find_all("div", class_=tag_class_name_low)[1].contents[0].strip()
                    )
                    week_52_high = self._float_normalizer(
                        soup.find_all("div", class_=tag_class_name_high)[1].contents[0].strip()
                    )
                    week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)
                except IndexError:
                    week_profit = 0

                self.data_table.append(
                    {
                        "code": code,
                        "name": name,
                        "growth": percentage,
                        "price": price,
                        "PE": p_e,
                        "max_profit": week_profit,
                    }
                )

    async def _table_builder(self):
        """Async task scheduler"""
        connector = aiohttp.TCPConnector(limit=500, limit_per_host=200, force_close=False, enable_cleanup_closed=True)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for corp in self.src_data:
                link = corp["link"]
                percentage = corp["percentage"]
                task = asyncio.create_task(self._get_corp_data(session, link, percentage, self.rate))
                tasks.append(task)
            await asyncio.gather(*tasks)


if __name__ == "__main__":

    new_table = CorpoUrlsGetter()

    start = time.time()
    corp_data = CompanyDataTableAsync(new_table)
    end = time.time() - start
    print(end)

    top = corp_data.generate_top_ten("price")
    print()
