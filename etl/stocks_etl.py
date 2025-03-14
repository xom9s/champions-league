from components import requests, get_connection, STOCKS
from typing import Optional, Dict, Any

STOCKS_API_URL = 'https://financialmodelingprep.com/api/v3/stock/full/real-time-price/INTERUSD'


def get_stocks() -> Optional[Dict[str, Any]]:
    
    uri = f'{STOCKS_API_URL}?apikey={STOCKS}'

    try:
        response = requests.get(uri) 
        response.raise_for_status()   
        return response.json()

    except (requests.RequestException, ValueError) as e:
         print(f"Error fetching stocks data: {e}")
         return None

def load_stocks_to_db() -> None:
    data = get_stocks()
    if not data:
        return
    
    conn = get_connection()
    if not conn:
        return

    with conn.cursor() as cur:
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
            
            if all([symbol, last_price, volume, last_updated]):
                cur.execute("""INSERT INTO stocks (symbol, last_price, volume, last_updated) VALUES (%s, %s, %s, %s);""", (symbol, last_price, volume, last_updated))


        
    conn.commit()
    cur.close()
    conn.close()
    print("Stock data successfully loaded")


if __name__ == "__main__":
    load_stocks_to_db()