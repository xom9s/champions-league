import requests
import json

def get_squads():
    with open ('config.json', 'r') as config_file:
        config = json.load(config_file)

    FOOTBALL_DATA = config['FOOTBALL_DATA']

    uri = 'https://api.football-data.org/v4/competitions/SA/teams'
    headers = {'X-Auth-Token':FOOTBALL_DATA}

    squads = requests.get(uri, headers=headers)
    
    for squad in squads.json()['teams']:
        print(squad['squad'])
if __name__ == '__main__':
    get_squads()