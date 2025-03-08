from . import json, requests, FOOTBALL_DATA

def get_matches():

    uri = 'https://api.football-data.org/v4/competitions/SA/matches'
    headers = { 'X-Auth-Token': FOOTBALL_DATA }

    matches = requests.get(uri, headers=headers)
    for match in matches.json()['matches']:
        print(match)

if __name__ == '__main__':
    get_matches()