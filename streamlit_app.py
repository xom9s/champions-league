import streamlit as st
from components.standings import get_standings

def display_standings():
    standings = get_standings()
    for standing in standings:
        st.write(standing['table'])

if __name__ == '__main__':
    display_standings()