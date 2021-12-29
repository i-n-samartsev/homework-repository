"""
### Homework
Ваша задача спарсить информацию о компаниях, находящихся в индексе
S&P 500 с данного сайта: <br>
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:
* Текущая стоимость в рублях (конвертацию производить по текущему курсу,
взятому с сайта [центробанка РФ](http://www.cbr.ru/development/sxml/))
* Код компании (справа от названия компании на странице компании)
* P/E компании (информация находится справа от графика на странице компании)
* Годовой рост/падение компании в процентах (основная таблица)
* Высчитать какую прибыль принесли бы акции компании (в процентах),
если бы они были куплены на уровне 52 Week Low и проданы на уровне
52 Week High (справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:
1. Топ 10 компаний с самими дорогими акциями в рублях.
2. Топ 10 компаний с самым низким показателем P/E.
3. Топ 10 компаний, которые показали самый высокий рост за последний год
4. Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были
куплены на самом минимуме и проданы на самом максимуме за последний год.
<br>Пример формата:
```
[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]
```
For scrapping you cans use `beautifulsoup4` <br>
For requesting `aiohttp`
"""
import asyncio
import datetime
from functools import lru_cache

import aiohttp
import bs4
import requests

COMPANIES_LIST_URLS = [
    f"https://markets.businessinsider.com/index/components/s&p_500?p={url}"
    for url in range(1, 11)
]


@lru_cache(1)
def get_usd_to_rub() -> float:
    today = datetime.date.today().strftime("%d/%m/%Y")
    usd_to_rub = requests.get(
        "http://www.cbr.ru/scripts/XML_dynamic.asp"
        f"?date_req1={today}&date_req2={today}&VAL_NM_RQ=R01235"
    )
    return float(
        usd_to_rub.text.split("<Value>")[1].split("<")[0].replace(",", ".")
    )


async def fetch_response(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return text


async def fetch_responses(urls: list[str]) -> list[str]:
    tasks = [asyncio.create_task(fetch_response(url)) for url in urls]
    await asyncio.gather(*tasks)
    return [task.result() for task in tasks]


def parse_companies_list(data: str) -> list[dict]:
    soup = BeautifulSoup(data, "html.parser")
    table = soup.find("tbody")
    companies_data = dict()
    companies_data["name"] = [link.get("title") for link in table.find_all("a")]
    companies_data["growth"] = [
        str(
            soup.select(
                f".table__tbody > tr:nth-child({n})"
                "> td:nth-child(8) > span:nth-child(3)"
            )
        )[-14:-9].strip(">")
        for n, _ in enumerate(soup.find_all("tr"), 1)
    ]
    companies_data["url"] = [
        f"https://markets.businessinsider.com{link.get('href')}"
        for link in table.find_all("a")
    ]
    return [
        {"name": name, "url": url, "growth": growth}
        for name, growth, url in zip(*companies_data.values())
    ]


def get_price(soup: bs4.BeautifulSoup) -> float:
    try:
        return round(
            float(
                soup.find("span", class_="price-section__current-value")
                .get_text()
                .replace(",", "")
            )
            * get_usd_to_rub(),
            2,
        )
    except AttributeError:
        return 0


def get_high_52(soup: bs4.BeautifulSoup) -> float:
    try:
        return float(
            soup.find("div", text="52 Week High")
            .previous_element.strip()
            .replace(",", "")
        )
    except AttributeError:
        return 0


def get_low_52(soup: bs4.BeautifulSoup) -> float:
    try:
        return float(
            soup.find("div", text="52 Week Low")
            .previous_element.strip()
            .replace(",", "")
        )
    except AttributeError:
        return 0


def get_p_e(soup: bs4.BeautifulSoup) -> float:
    try:
        return float(
            soup.find("div", text="P/E Ratio")
            .previous_element.strip()
            .replace(",", "")
        )
    except AttributeError:
        return 0


def parse_company_page(data: str) -> dict:
    soup = bs4.BeautifulSoup(data, "html.parser")
    company_data = dict()
    company_data["code"] = soup.title.get_text().split()[0]
    company_data["price"] = get_price(soup)
    company_data["p_e"] = get_p_e(soup)
    low_52 = get_low_52(soup)
    high_52 = get_high_52(soup)
    company_data["lost_profit"] = round(high_52 - low_52, 2)
    return company_data


async def dict_constructor() -> list[dict]:
    companies_lists = await fetch_responses(companies_list_urls)
    companies_dicts = []
    for companies_list in companies_lists:
        companies_dicts += parse_companies_list(companies_list)

    companies_urls = [
        company_data.pop("url") for company_data in companies_dicts
    ]
    companies_pages = await fetch_responses(companies_urls)
    for company_page, company_dict in zip(companies_pages, companies_dicts):
        company_data = parse_company_page(company_page)
        company_dict |= company_data

    return companies_dicts
