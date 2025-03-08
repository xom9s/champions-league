import requests
import json

with open('config.json', 'r') as config_file:
        config = json.load(config_file)

FOOTBALL_DATA = config['FOOTBALL_DATA']