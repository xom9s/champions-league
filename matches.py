import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

FOOTBALL_DATA = config['FOOTBALL_DATA']

uri = 'https://api.football-data.org/v4/competitions/CL/matches'
headers = { 'X-Auth-Token': FOOTBALL_DATA }

response = requests.get(uri, headers=headers)
for match in response.json()['matches']:
    print(match)