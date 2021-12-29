"""
    Ваша задача спарсить информацию о компаниях, находящихся в индексе S&P 500 с данного сайта:
    https://markets.businessinsider.com/index/components/s&p_500

    Подробно про задание:
    https://github.com/lex-av/epam_python_autumn_2020/blob/main/lecture_10_parallelization/hw/stonks.md
"""


import asyncio
import json
import time
from multiprocessing import Pool

import aiohttp
import xmltodict

from homework10.pack_task1.connection_utils import (
    get_base_response_text,
    get_page_count,
    get_page_links,
)
from homework10.pack_task1.parse_utils import (
    corp_code_parse,
    corp_max_profit_parse,
    corp_name_parse,
    corp_pe_parse,
    corp_price_parse,
    urls_growth_parse,
)


class MarketsInsiderRawData:
    """Class for getting all the data as responses.text"""

    def __init__(self, fixed_page_count=None):
        self.fixed_page_count = fixed_page_count

        self.base_resp_text = get_base_response_text()
        self.page_count = get_page_count(self.base_resp_text, self.fixed_page_count)
        self.page_links = get_page_links(self.page_count)
        self.pages_text_data = self._build_response_list(self.page_links)

        self.links_growth_data = []
        for text_data in self.pages_text_data:
            self.links_growth_data += urls_growth_parse(text_data)

        self.details_links = [corp["url"] for corp in self.links_growth_data]
        self.growth_values = [corp["year_growth"] for corp in self.links_growth_data]
        self.details_text_data = self._build_response_list(self.details_links)

    @staticmethod
    async def _get_request_text(session, url):
        async with session.get(url) as resp:
            if resp.status == 200:
                return await resp.text()

    async def _get_multiple_requests_text(self, url_list):
        async with aiohttp.ClientSession() as session:
            task_list = []
            for url in url_list:
                task = asyncio.create_task(self._get_request_text(session, url))
                task_list.append(task)
            return await asyncio.gather(*task_list)

    def _build_response_list(self, url_list):
        return asyncio.run(self._get_multiple_requests_text(url_list))


class CorpDataParser:
    """Class to process and present data from MarketInsider"""

    def __init__(self, details_text_data, growth_table, cpu_count=6):
        self.cpu_count = cpu_count
        self.details_text_data = details_text_data
        self.growth_table = growth_table
        self.rub_rate = self._get_rate()

        self.corp_names = []
        self.corp_codes = []
        self.corp_prices = []
        self.pe_vals = []
        self.corp_max_profit_vals = []

        self.data_table = []

    def _get_rate(self):
        """Return valute rate for current date"""
        data = asyncio.run(self._get_req())
        rate_data = xmltodict.parse(data)
        usd = float(rate_data["ValCurs"]["Valute"][10]["Value"].replace(",", "."))
        return usd

    @staticmethod
    async def _get_req():
        """aiohttp getter for valute rate xml-data from bank api"""
        async with aiohttp.ClientSession() as session:
            async with session.get("http://www.cbr.ru/scripts/XML_daily.asp") as resp:
                response = await resp.text()
                return response

    def compute_data(self):
        with Pool(self.cpu_count) as p:
            self.corp_names = p.map(corp_name_parse, self.details_text_data)
            self.corp_codes = p.map(corp_code_parse, self.details_text_data)
            self.corp_prices = p.starmap(
                corp_price_parse, zip(self.details_text_data, [self.rub_rate] * len(self.details_text_data))
            )
            self.pe_vals = p.map(corp_pe_parse, self.details_text_data)
            self.corp_max_profit_vals = p.map(corp_max_profit_parse, self.details_text_data)

        # with Pool(self.cpu_count) as p:
        #     self.corp_codes = p.map(pu.corp_code_parse, self.details_text_data)
        # with Pool(self.cpu_count) as p:
        #     self.corp_prices = p.starmap(
        #         pu.corp_price_parse, zip(self.details_text_data, [self.rub_rate] * len(self.details_text_data))
        #     )
        # with Pool(self.cpu_count) as p:
        #     self.pe_vals = p.map(pu.corp_pe_parse, self.details_text_data)
        # with Pool(self.cpu_count) as p:
        #     self.corp_max_profit_vals = p.map(pu.corp_max_profit_parse, self.details_text_data)

    def build_data_table(self):
        for name, code, price, pe, max_profit, growth in zip(
            self.corp_names,
            self.corp_codes,
            self.corp_prices,
            self.pe_vals,
            self.corp_max_profit_vals,
            self.growth_table,
        ):

            self.data_table.append(
                {
                    "code": code,
                    "name": name,
                    "price": price,
                    "growth": growth,
                    "PE": pe,
                    "max_profit": max_profit,
                }
            )

    def generate_top(self, parameter, rev=True, length=10):
        """
        Generates top ten corps from data_table by given parameter
        Cleans table from line with None values
        """
        remove_indexes = []

        for index, corp_data in enumerate(self.data_table):
            if corp_data["price"] is None or corp_data["PE"] is None or corp_data["max_profit"] is None:
                remove_indexes.append(index)
        for index in sorted(remove_indexes, reverse=True):
            self.data_table.pop(index)

        return sorted(self.data_table, key=lambda row: row[parameter], reverse=rev)[:length]

    @staticmethod
    def json_writer(dict_list, report_name):
        """Generates json-file, based on given report"""

        file_name = report_name + ".json"
        with open(file_name, "w") as report:
            json.dump(dict_list, report, indent=2)


if __name__ == "__main__":
    start = time.time()
    raw_data = MarketsInsiderRawData()
    end = time.time() - start
    print(end)

    start = time.time()
    table_data = CorpDataParser(raw_data.details_text_data, raw_data.growth_values)
    table_data.compute_data()
    table_data.build_data_table()
    end = time.time() - start
    print(end)

    top_price = table_data.generate_top("price", length=10)
    top_low_pe = table_data.generate_top("PE", rev=False, length=10)
    top_growth = table_data.generate_top("growth", length=10)
    top_max_profit = table_data.generate_top("max_profit", length=10)

    table_data.json_writer(top_price, "rep1_price")
    table_data.json_writer(top_low_pe, "rep2_pe")
    table_data.json_writer(top_growth, "rep3_growth")
    table_data.json_writer(top_max_profit, "rep4_profit")

    print()
