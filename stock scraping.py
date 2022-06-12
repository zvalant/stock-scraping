import requests
from datetime import datetime
import time
def stockscrape():
    ticker = input("Enter Ticker: ")
    date_start =int(time.mktime(datetime.strptime(input("Enter start date in yyyy/mm/dd format: "),"%Y/%m/%d").timetuple()))
    date_stop =int(time.mktime(datetime.strptime(input("Enter stop date in yyyy/mm/dd format: "), "%Y/%m/%d").timetuple()))
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={date_start}&period2={date_stop}&interval=1d&events=history&includeAdjustedClose=true"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
    content = requests.get(url, headers=headers).content
    with open(f"{ticker}.csv", "wb") as file:
        file.write(content)
    return ticker

