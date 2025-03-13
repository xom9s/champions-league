import requests
import json
import psycopg2
import streamlit as st
import pandas as pd

with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        
STOCKS = config['STOCKS']
FOOTBALL_DATA = config['FOOTBALL_DATA']
NEWS_API_KEY = config['NEWS']
DB_CONFIG = config['DB_CONFIG']

def get_connection():
        try:
                conn = psycopg2.connect(**DB_CONFIG)
                return conn
        except psycopg2.Error as e:
                print(f"Error has occured {e}")