'''
Author: your name
Date: 2021-08-03 07:33:07
LastEditTime: 2021-08-03 08:18:36
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /binance-public-data-1/python/enums.py
'''
from datetime import *

YEARS = ['2017', '2018', '2019', '2020', '2021']
INTERVALS = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1mo"]
DAILY_INTERVALS = ["1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d"]
MONTHS = list(range(1,13))
MAX_DAYS = 500
BASE_URL = 'https://data.binance.vision/'
START_DATE = date(int(YEARS[0]), MONTHS[0], 1)
END_DATE = datetime.date(datetime.now())