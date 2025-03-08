from . import json, requests, FOOTBALL_DATA

def get_teams():

    uri = 'https://api.football-data.org/v4/competitions/SA/teams'
    headers = { 'X-Auth-Token': FOOTBALL_DATA }
    teams = requests.get(uri, headers=headers)
    for team in teams.json()['teams']:
        print(team['shortName'])

if __name__ == '__main__':
    get_teams()