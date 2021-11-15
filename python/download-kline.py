import sys,os
from datetime import *
import pandas as pd
from enums import *
from utility import download_file, get_all_symbols, get_parser, get_start_end_date_objects, convert_to_date_object
from dateutil.relativedelta import relativedelta

def download_monthly_klines(symbols, num_symbols, intervals, years, months, start_date, end_date, folder, checksum):
  current = 0
  date_range = None

  if start_date and end_date:
    date_range = start_date + " " + end_date

  if not start_date:
    start_date = START_DATE
  else:
    start_date = convert_to_date_object(start_date)

  if not end_date:
    end_date = END_DATE
  else:
    end_date = convert_to_date_object(end_date)

  print("Found {} symbols".format(num_symbols))
  import datetime
  for symbol in symbols:
    print("[{}/{}] - start download monthly {} klines ".format(current+1, num_symbols, symbol))
    for interval in intervals:
      for year in years:
        for month in months:
          cur_year = datetime.datetime.now().year
          cur_month = datetime.datetime.now().month
          if str(year) >= str(cur_year) and month >= cur_month:
            return
          current_date = convert_to_date_object('{}-{}-01'.format(year, month))
          if current_date >= start_date and current_date <= end_date:
            path = "data/spot/monthly/klines/{}/{}/".format(symbol.upper(), interval)
            file_name = "{}-{}-{}-{}.zip".format(symbol.upper(), interval, year, '{:02d}'.format(month))
            download_file(path, file_name, date_range, folder)

            if checksum == 1:
              checksum_path = "data/spot/monthly/klines/{}/{}/".format(symbol.upper(), interval)
              checksum_file_name = "{}-{}-{}-{}.zip.CHECKSUM".format(symbol.upper(), interval, year, '{:02d}'.format(month))
              download_file(checksum_path, checksum_file_name, date_range, folder)
    
    current += 1

def download_daily_klines(symbols, num_symbols, intervals, dates, start_date, end_date, folder, checksum):
  current = 0
  date_range = None

  if start_date and end_date:
    date_range = start_date + " " + end_date

  if not start_date:
    start_date = START_DATE
  else:
    start_date = convert_to_date_object(start_date)

  if not end_date:
    end_date = END_DATE
  else:
    end_date = convert_to_date_object(end_date)

  #Get valid intervals for daily
  intervals = list(set(intervals) & set(DAILY_INTERVALS))
  print("Found {} symbols".format(num_symbols))

  for symbol in symbols:
    print("[{}/{}] - start download daily {} klines ".format(current+1, num_symbols, symbol))
    for interval in intervals:
      for date in dates:
        current_date = convert_to_date_object(date)
        if current_date >= start_date and current_date <= end_date:
          path = "data/spot/daily/klines/{}/{}/".format(symbol.upper(), interval)
          file_name = "{}-{}-{}.zip".format(symbol.upper(), interval, date)
          download_file(path, file_name, date_range, folder)

          if checksum == 1:
            checksum_path = "data/spot/daily/klines/{}/{}/".format(symbol.upper(), interval)
            checksum_file_name = "{}-{}-{}.zip.CHECKSUM".format(symbol.upper(), interval, date)
            download_file(checksum_path, checksum_file_name, date_range, folder)
    current += 1

    
if __name__ == "__main__":
    parser = get_parser('klines')
    args = parser.parse_args(sys.argv[1:])
    args.intervals = ['4h']
    from dateutil.relativedelta import relativedelta
    args.years = ['2018','2019','2020','2021']
    d = date.today() - relativedelta(months=+1)
    args.years= [d.year]
    args.months = [9,10]
    # args.folder = os.path.join(os.path.expanduser('~'))
    if not args.symbols:
      print("fetching all symbols from exchange")
      symbols = get_all_symbols()
      num_symbols = len(symbols)
    else:
      symbols = args.symbols
      num_symbols = len(symbols)
    
    if args.dates:
      dates = args.dates
    else:
      dates = pd.date_range(end = datetime.today(), periods = MAX_DAYS).to_pydatetime().tolist()
      dates = [date.strftime("%Y-%m-%d") for date in dates]
      download_monthly_klines(symbols, num_symbols, args.intervals, args.years, args.months, args.startDate, args.endDate, args.folder, args.checksum)
    #download_daily_klines(symbols, num_symbols, args.intervals, dates, args.startDate, args.endDate, args.folder, args.checksum)
    
