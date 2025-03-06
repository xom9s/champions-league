import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

FOOTBALL_DATA = config['FOOTBALL_DATA']

uri = 'https://api.football-data.org/v4/competitions/SA/standings'
headers = { 'X-Auth-Token': FOOTBALL_DATA}

standings = requests.get(uri, headers=headers)
for standing in standings.json()['standings']:
    print(standing['table'])

