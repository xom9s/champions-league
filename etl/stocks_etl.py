from components import requests, get_connection, STOCKS


def get_stocks():
    
    uri = f'https://financialmodelingprep.com/api/v3/stock/full/real-time-price/INTERUSD?apikey={STOCKS}'

    stocks_info = requests.get(uri)

    if stocks_info.status_code == 200:
        return stocks_info.json()


    else:
         print(f"Error: {stocks_info.status_code}")

def load_stocks_to_db():
    data = get_stocks()
    conn = get_connection()

    if not conn:
        return
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS stocks ( id SERIAL PRIMARY KEY,
        symbol VARCHAR(10),
        last_price FLOAT,
        volume INT,
        last_updated BIGINT);""")
    if data:
        stock = data[0]
        symbol = stock["symbol"]
        last_price = stock["lastSalePrice"]
        volume = stock["volume"]
        last_updated = stock["lastUpdated"]
    
        

        cur.execute("""INSERT INTO stocks (symbol, last_price, volume, last_updated) VALUES (%s, %s, %s, %s);""", (symbol, last_price, volume, last_updated))


    
        conn.commit()
        cur.close()
        conn.close()
        print("Stock data successfully loaded")


if __name__ == "__main__":
    load_stocks_to_db()