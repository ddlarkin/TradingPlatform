# Downloads all simple stock info to the database for storage for the suggestion info.
#

import mariadb
import APIInfo
import requests
import time
import json
import datetime as dt

db = mariadb.connect(
    user="root",
    password="Inuvik",
    host="localhost",
    port=3306,
    database="stockSuggestionInfo"

)

myCursor = db.cursor(buffered=True)
myCursor.execute("USE stockSuggestionInfo;")


def getTickersCompanyName():
    apiKey = APIInfo.info('KEY')
    apiBase = APIInfo.info('BASE')
    currentURL = f'{apiBase}/v3/reference/tickers?&limit=1000&market=stocks&apiKey={apiKey}'
    data = requests.get(currentURL).json()

    for i in data['results']:
        print(f'INSERT INTO stockInfo (Ticker, CompanyName, Volume, Price) values ("{i["ticker"]}", "{i["name"]}", NULL, NULL);')

        myCursor.execute(f'INSERT INTO stockInfo (Ticker, CompanyName, Volume, Price) values ("{i["ticker"]}", "{i["name"]}", NULL, NULL);')
        db.commit()

    myCursor.execute("SELECT COUNT(*) FROM stockInfo;")
    noRows = myCursor.fetchall()[0][0]

    # This loop repeats as long as the received data comes in batches of 1000, ends when all data has been received.
    while noRows % 1000 == 0:

        # Uses the next_url to continue getting data.
        currentURL = data['next_url'] + f'&apiKey={apiKey}'
        # As the current plan only allows 5 requests per minute this is added to prevent failures.
        startTime = dt.datetime.now()

        data = requests.get(currentURL).json()
        print(data)
        for i in data['results']:
            print(f'INSERT INTO stockInfo (Ticker, CompanyName, Volume, Price) values ("{i["ticker"]}", {json.dumps(i["name"])}, NULL, NULL);')
            myCursor.execute(f'INSERT INTO stockInfo (Ticker, CompanyName, Volume, Price) values ("{i["ticker"]}", {json.dumps(i["name"])}, NULL, NULL);')
            db.commit()

        # Uses the previous generated time to ensure the max request speed is 4/min.
        while dt.datetime.now() <= startTime + dt.timedelta(0, 15):
            time.sleep(1)

        myCursor.execute("SELECT COUNT(*) FROM stockInfo;")
        noRows = myCursor.fetchall()[0][0]


def getPriceVolume(date='2022-11-04', adjusted='true'):
    apiKey = APIInfo.info('KEY')
    apiBase = APIInfo.info('BASE')
    currentURL = f'{apiBase}/v2/aggs/grouped/locale/us/market/stocks/{date}?adjusted={adjusted}&apiKey={apiKey}'
    data = requests.get(currentURL).json()
    for i in data['results']:
        print(f'Ticker = {i["T"]}, Volume = {i["v"]}, closePrice = {i["c"]}')
        myCursor.execute(f"UPDATE stockInfo SET Volume = {i['v']}, Price = {i['c']} WHERE Ticker = '{i['T']}';")
        db.commit()


getTickersCompanyName()
getPriceVolume()
myCursor.execute("DELETE FROM stockInfo WHERE PRICE = '' OR PRICE IS NULL;")
db.commit()
