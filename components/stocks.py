import streamlit as st
import pandas as pd
from etl.stocks_etl import get_stocks


def display_stocks():
    data = get_stocks()

    if data:
        stocks_data = []
        for stock in data:
            stocks_data.append({
                'Symbol': stock['symbol'],
                'Last Price': stock['lastSalePrice'],
                'Volume': stock['volume'],
                'Last Updated': stock['lastUpdated']
            })
        df = pd.DataFrame(stocks_data)
        st.write("### Stock data")
        st.table(df)
    else:
        st.write("No stock data available.")


if __name__ == "__main__":
    display_stocks()