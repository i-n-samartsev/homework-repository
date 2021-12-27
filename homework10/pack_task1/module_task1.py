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
from bs4 import BeautifulSoup


class NetworkException:
    """Resource is not available"""


class CorpoUrlsGetter:
    """Container to get and store corps pre-names, urls and year percent"""

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
        # Corp = namedtuple("Corp", "url percent")  # Corp._make([])
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
    """

    def __init__(self, table_src):
        self.table_data = table_src
        self.corp_table = []
        asyncio.run(self.table_builder())

    @staticmethod
    def float_normalizer(value_in_str):
        """Converts given str from web-page to float"""
        if "," in value_in_str:
            lst_repr = value_in_str.strip("%").split(",")
            return float("".join(lst_repr))
        return float(value_in_str.strip())

    async def get_corp_data(self, session, url, percentage):
        async with session.get(url) as response:
            if response.status != 200:
                self.corp_table.append({"code": None, "name": None, "growth": -1, "PE": -1, "max_profit": -1})
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
                    p_e = self.float_normalizer(
                        soup.find("div", text=re.compile("P/E Ratio")).parent.text.strip().strip("P/E Ratio").strip()
                    )
                except AttributeError:
                    p_e = -1

                tag_class_name_low = "snapshot__data-item snapshot__data-item--small"
                tag_class_name_high = "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"

                try:
                    week_52_low = self.float_normalizer(soup.find("div", class_=tag_class_name_low).contents[0].strip())
                    week_52_high = self.float_normalizer(
                        soup.find("div", class_=tag_class_name_high).contents[0].strip()
                    )
                    week_profit = round(((week_52_high - week_52_low) / week_52_low) * 100, 2)
                except Exception:
                    week_profit = 0

                self.corp_table.append(
                    {"code": code, "name": name, "growth": percentage, "PE": p_e, "max_profit": week_profit}
                )

    async def table_builder(self):
        connector = aiohttp.TCPConnector(limit=50)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            for corp in self.table_data:
                link = corp["link"]
                percentage = corp["percentage"]
                task = asyncio.create_task(self.get_corp_data(session, link, percentage))
                tasks.append(task)
            await asyncio.gather(*tasks)


class CompanyDataTableThreads:
    """
    Collection to store S&P-500 corps parameters
    Gets Urls/percentage table-object from CorpoUrlsGetter
    """

    def __init__(self, table_src):
        self.table_data = table_src
        self.soup_table = []
        self.url_list = [corp["link"] for corp in self.table_data]
        self.table_builder()

    def fetch_page(self, corp):
        url = corp["link"]
        percentage = corp["percentage"]
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        code = soup.find("span", class_="price-section__category").find("span").contents[0]
        name = soup.find("span", class_="price-section__label").contents[0]
        self.soup_table.append({"code": code, "name": name, "grouth": percentage})
        print(name)

    def table_builder(self):
        with ThreadPool(10) as t_pool:
            t_pool.map(self.fetch_page, self.table_data)


if __name__ == "__main__":

    new_table = CorpoUrlsGetter()

    start = time.time()
    corp_data = CompanyDataTableAsync(new_table[:497])
    end = time.time() - start

    print(end)
    # for company in new_table:
    #     if company["link"] == "https://markets.businessinsider.com/stocks/mmm-stock":
    #         print(company["link"], company["percentage"])

    print()
