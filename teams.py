import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

FOOTBALL_DATA = config['FOOTBALL_DATA']

uri = 'https://api.football-data.org//v4/competitions/CL/teams'
headers = { 'X-Auth-Token': FOOTBALL_DATA }
teams = requests.get(uri, headers=headers)
for team in teams.json()['teams']:
    print(team['shortName'])
