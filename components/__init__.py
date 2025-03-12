import requests
import json
import psycopg2

with open('config.json', 'r') as config_file:
        config = json.load(config_file)

FOOTBALL_DATA = config['FOOTBALL_DATA']
NEWS_API_KEY = config['NEWS']