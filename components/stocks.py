from . import json, requests, psycopg2, STOCKS


def get_stocks():
    uri = f'https://financialmodelingprep.com/api/v3/stock/full/real-time-price/INTERUSD?apikey={STOCKS}'

    stocks_info = requests.get(uri)

    return stocks_info.json()

if __name__ == "__main__":
    get_stocks()