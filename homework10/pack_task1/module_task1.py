"""
    Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
    https://markets.businessinsider.com/index/components/s&p_500

    Подробно про задание:
    https://github.com/lex-av/epam_python_autumn_2020/blob/main/lecture_10_parallelization/hw/stonks.md
"""


# from collections import namedtuple
from multiprocessing.pool import ThreadPool

import requests
from bs4 import BeautifulSoup


class CorpoUrlsGetter:
    """Container to get and store corps pre-names, urls and year percent"""

    def __init__(self, url="https://markets.businessinsider.com/index/components/s&p_500?p=", pages_count=11):
        self.domain = "https://markets.businessinsider.com"
        self.pages_count = pages_count
        self.pages_list = [url + str(page_number) for page_number in range(1, self.pages_count + 1)]
        self.corp_table = []
        self.table_cursor = 0
        self.table_builder_threading()

    def __getitem__(self, index):
        if index < len(self.corp_table):
            return self.corp_table[index]
        else:
            raise IndexError

    def __next__(self):
        if len(self.corp_table) > self.table_cursor:
            value = self.corp_table[self.table_cursor]
            self.table_cursor += 1
            return value
        else:
            raise StopIteration

    def __iter__(self):
        return self

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

        for row in rows:
            percentage_cell = row.find_all("td")[7]
            cell_value = percentage_cell.find_all("span")[0]
            percentage_value = cell_value.contents[0]
            percentages.append(percentage_value)

        for link, percentage in zip(links, percentages):
            # page_data.append(Corp._make([link, percentage]))
            page_data.append({"link": link, "percentage": percentage})

        self.corp_table += page_data

    def table_builder_threading(self):
        with ThreadPool(self.pages_count) as t_pool:
            t_pool.map(self.append_page_data, self.pages_list)


if __name__ == "__main__":

    new_table = CorpoUrlsGetter()
    print()
