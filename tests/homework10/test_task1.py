import asyncio
import heapq
import json
import os

from homework10.task1 import dict_constructor

test_data_dict = {
    "p_e": [{'name': 'Vornado Realty Trust', 'growth': '12.63', 'code': 'VNO', 'price': 3123.56, 'p_e': -893.45, 'lost_profit': 15.87}, {'name': 'Chevron', 'growth': '39.92', 'code': 'CVX', 'price': 8657.72, 'p_e': -427.45, 'lost_profit': 35.45}, {'name': 'Devon Energy', 'growth': '90.55', 'code': 'DVN', 'price': 3240.66, 'p_e': -167.13, 'lost_profit': 30.31}, {'name': 'ExxonMobil', 'growth': '48.33', 'code': 'XOM', 'price': 4494.21, 'p_e': -125.36, 'lost_profit': 25.41}, {'name': 'Phillips 66', 'growth': '4.96', 'code': 'PSX', 'price': 5350.77, 'p_e': -76.53, 'lost_profit': 31.14}, {'name': 'Under Armour', 'growth': '21.02', 'code': 'UAA', 'price': 1566.57, 'p_e': -64.5, 'lost_profit': 10.32}, {'name': 'Incyte', 'growth': '14.32', 'code': 'INCY', 'price': 5516.49, 'p_e': -63.09, 'lost_profit': 39.56}, {'name': 'Twitter', 'growth': '18.59', 'code': 'TWTR', 'price': 3281.91, 'p_e': -62.1, 'lost_profit': 39.73}, {'name': 'Moderna', 'growth': '21.62', 'code': 'MRNA', 'price': 18352.46, 'p_e': -59.95, 'lost_profit': 394.51}, {'name': 'Under Armour', 'growth': '18.44', 'code': 'UA', 'price': 1332.35, 'p_e': -55.67, 'lost_profit': 8.36}]
,
    "price": [{'name': 'NVR', 'growth': '40.22', 'code': 'NVR', 'price': 436086.26, 'p_e': 17.87, 'lost_profit': 2093.16}, {'name': 'Amazon', 'growth': '3.33', 'code': 'AMZN', 'price': 250317.54, 'p_e': 79.54, 'lost_profit': 892.08}, {'name': 'Alphabet A', 'growth': '66.75', 'code': 'GOOGL', 'price': 216202.95, 'p_e': 30.0, 'lost_profit': 1322.72}, {'name': 'Alphabet C', 'growth': '66.73', 'code': 'GOOG', 'price': 215677.08, 'p_e': 30.01, 'lost_profit': 1337.33}, {'name': 'Booking Holdings', 'growth': '12.00', 'code': 'BKNG', 'price': 177738.5, 'p_e': 460.92, 'lost_profit': 826.56}, {'name': 'AutoZone', 'growth': '71.72', 'code': 'AZO', 'price': 153621.35, 'p_e': 16.27, 'lost_profit': 1002.36}, {'name': 'Chipotle Mexican Grill', 'growth': '26.14', 'code': 'CMG', 'price': 129179.4, 'p_e': 129.05, 'lost_profit': 702.28}, {'name': 'Mettler-Toledo International', 'growth': '47.71', 'code': 'MTD', 'price': 125080.7, 'p_e': 43.78, 'lost_profit': 677.5}, {'name': 'Tesla', 'growth': '64.83', 'code': 'TSLA', 'price': 80487.72, 'p_e': 299.31, 'lost_profit': 704.0}, {'name': 'BlackRock', 'growth': '29.83', 'code': 'BLK', 'price': 67472.78, 'p_e': 20.99, 'lost_profit': 302.72}]
,
    "growth": [{'name': 'CF Industries Holdings', 'growth': '98.47', 'code': 'CF', 'price': 5334.57, 'p_e': 24.94, 'lost_profit': 37.83}, {'name': 'APA Corporation Registered Shs', 'growth': '96.83', 'code': 'APA', 'price': 2010.68, 'p_e': -13.09, 'lost_profit': 17.11}, {'name': 'Extra Space Storage', 'growth': '94.73', 'code': 'EXR', 'price': 16587.77, 'p_e': 30.52, 'lost_profit': 119.64}, {'name': 'Applied Materials', 'growth': '91.73', 'code': 'AMAT', 'price': 11791.59, 'p_e': 0, 'lost_profit': 77.85}, {'name': 'Devon Energy', 'growth': '90.55', 'code': 'DVN', 'price': 3240.66, 'p_e': -167.13, 'lost_profit': 30.31}, {'name': 'Akamai', 'growth': '9.92', 'code': 'AKAM', 'price': 8679.08, 'p_e': 20.32, 'lost_profit': 32.27}, {'name': 'Baker Hughes', 'growth': '9.92', 'code': 'BKR', 'price': 1768.37, 'p_e': 684.57, 'lost_profit': 8.9}, {'name': 'Starbucks', 'growth': '9.47', 'code': 'SBUX', 'price': 8596.59, 'p_e': 29.83, 'lost_profit': 30.38}, {'name': 'Verisk Analytic a', 'growth': '9.34', 'code': 'VRSK', 'price': 16862.49, 'p_e': 40.63, 'lost_profit': 71.71}, {'name': 'Fortive', 'growth': '9.31', 'code': 'FTV', 'price': 5615.18, 'p_e': 32.41, 'lost_profit': 15.29}]
,
    "lost_profit": [{'name': 'NVR', 'growth': '40.22', 'code': 'NVR', 'price': 436086.26, 'p_e': 17.87, 'lost_profit': 2093.16}, {'name': 'Alphabet C', 'growth': '66.73', 'code': 'GOOG', 'price': 215677.08, 'p_e': 30.01, 'lost_profit': 1337.33}, {'name': 'Alphabet A', 'growth': '66.75', 'code': 'GOOGL', 'price': 216202.95, 'p_e': 30.0, 'lost_profit': 1322.72}, {'name': 'AutoZone', 'growth': '71.72', 'code': 'AZO', 'price': 153621.35, 'p_e': 16.27, 'lost_profit': 1002.36}, {'name': 'Amazon', 'growth': '3.33', 'code': 'AMZN', 'price': 250317.54, 'p_e': 79.54, 'lost_profit': 892.08}, {'name': 'Booking Holdings', 'growth': '12.00', 'code': 'BKNG', 'price': 177738.5, 'p_e': 460.92, 'lost_profit': 826.56}, {'name': 'Tesla', 'growth': '64.83', 'code': 'TSLA', 'price': 80487.72, 'p_e': 299.31, 'lost_profit': 704.0}, {'name': 'Chipotle Mexican Grill', 'growth': '26.14', 'code': 'CMG', 'price': 129179.4, 'p_e': 129.05, 'lost_profit': 702.28}, {'name': 'Mettler-Toledo International', 'growth': '47.71', 'code': 'MTD', 'price': 125080.7, 'p_e': 43.78, 'lost_profit': 677.5}, {'name': 'Moderna', 'growth': '21.62', 'code': 'MRNA', 'price': 18352.46, 'p_e': -59.95, 'lost_profit': 394.51}]
,
}


def get_top_10(companies_dicts, key: str, reverse=False) -> heapq:
    if reverse:
        return heapq.nlargest(10, companies_dicts, key=lambda x: -x.get(key, 0))
    return heapq.nlargest(10, companies_dicts, key=lambda x: x.get(key, 0))


async def main_task():
    companies_data = await dict_constructor()

    for key in ["price", "growth", "lost_profit"]:
        with open(f"top_10_{key}.json", "w") as file:
            top_10 = get_top_10(companies_data, key)
            json.dump(top_10, file, indent=4)

    with open("top_10_p_e.json", "w") as file:
        top_10 = get_top_10(companies_data, "p_e", reverse=True)
        json.dump(top_10, file, indent=4)


def test_main_task():
    asyncio.run(main_task())
    for key in ["price"]:
        with open(f"top_10_{key}.json") as fi:
            assert json.loads(fi.read()) == test_data_dict[key]
