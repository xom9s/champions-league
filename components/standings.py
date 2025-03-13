import streamlit as st
from etl.standings_etl import get_standings

def display_standings():
    standings = get_standings()
    for standing in standings:
        st.write("### Standings")
        st.write(standing['table'])
