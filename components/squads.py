from . import json, requests, FOOTBALL_DATA

def get_squads():
    
    uri = 'https://api.football-data.org/v4/competitions/SA/teams'
    headers = {'X-Auth-Token':FOOTBALL_DATA}

    squads = requests.get(uri, headers=headers)
    
    for squad in squads.json()['teams']:
        print(squad['squad'])
if __name__ == '__main__':
    get_squads()