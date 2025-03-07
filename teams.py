import requests
import json

def get_teams():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    FOOTBALL_DATA = config['FOOTBALL_DATA']

    uri = 'https://api.football-data.org/v4/competitions/SA/teams'
    headers = { 'X-Auth-Token': FOOTBALL_DATA }
    teams = requests.get(uri, headers=headers)
    for team in teams.json()['teams']:
        print(team['shortName'])

if __name__ == '__main__':
    get_teams()