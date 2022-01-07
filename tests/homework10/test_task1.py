import asyncio
import copy
import heapq
import json
import os

from homework10.task1 import create_companies_data

test_data_dict = {
    "p_e": [
        {"name": "Bath & Body Works", "code": "BBWI", "lost_profit": 0},
        {"name": "Honeywell", "code": "HON", "lost_profit": 0},
        {"name": "Organon & Company", "code": "OGN", "lost_profit": 0},
        {
            "name": "Seagate Technology Holdings",
            "code": "STX",
            "lost_profit": 0,
        },
        {"name": "Amcor", "code": "AMCR", "lost_profit": 2.59},
        {"name": "Huntington Bancstocks", "code": "HBAN", "lost_profit": 4.31},
        {"name": "PPL", "code": "PPL", "lost_profit": 4.57},
        {"name": "Kinder Morgan", "code": "KMI", "lost_profit": 5.63},
        {
            "name": "Hewlett Packard Enterprise",
            "code": "HPE",
            "lost_profit": 5.78,
        },
        {"name": "Host Hotels & Resorts", "code": "HST", "lost_profit": 5.86},
    ],
    "price": [
        {"name": "NVR", "code": "NVR", "price": 429279.75},
        {"name": "Amazon", "code": "AMZN", "price": 246535.5},
        {"name": "Alphabet A", "code": "GOOGL", "price": 206662.5},
        {"name": "Alphabet C", "code": "GOOG", "price": 206480.25},
        {"name": "Booking Holdings", "code": "BKNG", "price": 180997.5},
        {"name": "AutoZone", "code": "AZO", "price": 152442.0},
        {"name": "Chipotle Mexican Grill", "code": "CMG", "price": 119662.5},
        {
            "name": "Mettler-Toledo International",
            "code": "MTD",
            "price": 118747.5,
        },
        {"name": "Tesla", "code": "TSLA", "price": 81609.0},
        {"name": "BlackRock", "code": "BLK", "price": 66921.75},
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
        with open(os.getcwd() + f"\page_{i}.html") as fi:
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
    for key in ["growth", "p_e"]:
        with open(os.getcwd() + f"\top_10_{key}.json") as fi:
            assert json.loads(fi.read()) == test_data_dict[key]
