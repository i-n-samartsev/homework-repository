import asyncio
import copy
import heapq
import json
import os

from homework10.task1 import create_companies_data

test_data_dict = {
    "p_e": [
        {"name": "Vornado Realty Trust", "code": "VNO", "p_e": -893.45},
        {"name": "Chevron", "code": "CVX", "p_e": -427.45},
        {"name": "Devon Energy", "code": "DVN", "p_e": -167.13},
        {"name": "ExxonMobil", "code": "XOM", "p_e": -125.36},
        {"name": "Phillips 66", "code": "PSX", "p_e": -76.53},
        {"name": "Under Armour", "code": "UAA", "p_e": -64.5},
        {"name": "Incyte", "code": "INCY", "p_e": -63.09},
        {"name": "Twitter", "code": "TWTR", "p_e": -62.1},
        {"name": "Moderna", "code": "MRNA", "p_e": -59.95},
        {"name": "Under Armour", "code": "UA", "p_e": -55.67},
    ],
    "price": [
        {"name": "NVR", "code": "NVR", "price": 411042.0},
        {"name": "Amazon", "code": "AMZN", "price": 243303.0},
        {"name": "Alphabet C", "code": "GOOG", "price": 205053.0},
        {"name": "Alphabet A", "code": "GOOGL", "price": 204915.0},
        {"name": "Booking Holdings", "code": "BKNG", "price": 182858.25},
        {"name": "AutoZone", "code": "AZO", "price": 151247.25},
        {"name": "Chipotle Mexican Grill", "code": "CMG", "price": 120300.0},
        {
            "name": "Mettler-Toledo International",
            "code": "MTD",
            "price": 116502.0,
        },
        {"name": "Tesla", "code": "TSLA", "price": 76067.25},
        {"name": "BlackRock", "code": "BLK", "price": 66857.25},
    ],
    "growth": [
        {"name": "Arista Networks", "growth": "97.68", "code": "ANET"},
        {"name": "Extra Space Storage", "growth": "95.75", "code": "EXR"},
        {"name": "Baker Hughes", "growth": "9.92", "code": "BKR"},
        {"name": "Atmos Energy", "growth": "9.76", "code": "ATO"},
        {
            "name": "Huntington Ingalls Industries",
            "growth": "9.54",
            "code": "HII",
        },
        {"name": "General Electric", "growth": "9.38", "code": "GE"},
        {"name": "Starbucks", "growth": "9.34", "code": "SBUX"},
        {"name": "Stryker", "growth": "9.07", "code": "SYK"},
        {
            "name": "APA Corporation Registered Shs",
            "growth": "89.50",
            "code": "APA",
        },
        {"name": "Simon Property Group", "growth": "87.44", "code": "SPG"},
    ],
    "lost_profit": [
        {"name": "NVR", "code": "NVR", "lost_profit": 2093.16},
        {"name": "Alphabet C", "code": "GOOG", "lost_profit": 1337.33},
        {"name": "Alphabet A", "code": "GOOGL", "lost_profit": 1322.72},
        {"name": "AutoZone", "code": "AZO", "lost_profit": 1002.36},
        {"name": "Amazon", "code": "AMZN", "lost_profit": 892.08},
        {"name": "Booking Holdings", "code": "BKNG", "lost_profit": 826.56},
        {"name": "Tesla", "code": "TSLA", "lost_profit": 704.0},
        {
            "name": "Chipotle Mexican Grill",
            "code": "CMG",
            "lost_profit": 702.28,
        },
        {
            "name": "Mettler-Toledo International",
            "code": "MTD",
            "lost_profit": 681.35,
        },
        {"name": "Moderna", "code": "MRNA", "lost_profit": 389.97},
    ],
}


def get_top_10(companies_dicts, key: str) -> heapq:
    return heapq.nlargest(10, companies_dicts, key=lambda x: x.get(key, 0))


def get_less_10(companies_dicts, key: str) -> heapq:
    return heapq.nlargest(10, companies_dicts, key=lambda x: -x.get(key, 0))


def remove_not_indicator(company_data, indicator):
    keys = ["price", "growth", "lost_profit", "p_e"]
    keys.remove(indicator)
    for key in keys:
        company_data.pop(key)


def create_companies_data_indicator(companies_data, indicator: str):
    companies_data_ind = copy.deepcopy(companies_data)
    for company_data in companies_data_ind:
        remove_not_indicator(company_data, indicator)

    return companies_data_ind


async def main_task():
    test_data = []
    for i in range(0, 10):
        with open(os.getcwd() + f"/tests/homework10/page_{i}.html") as fi:
            test_data.append(fi.read())
    companies_data = await create_companies_data(test_data)

    for key in ["price", "growth", "lost_profit"]:
        companies_data_ind = create_companies_data_indicator(
            companies_data, key
        )
        with open(f"top_10_{key}.json", "w") as file:
            top_10 = get_top_10(companies_data_ind, key)
            json.dump(top_10, file, indent=4)

    companies_data_ind = create_companies_data_indicator(companies_data, "p_e")
    with open("less_10_p_e.json", "w") as file:
        less_10 = get_less_10(companies_data_ind, "p_e")
        json.dump(less_10, file, indent=4)


def test_main_task():
    asyncio.run(main_task())
    for key in ["growth"]:
        with open(os.getcwd() + f"/tests/homework10/top_10_{key}.json") as fi:
            assert json.loads(fi.read()) == test_data_dict[key]
