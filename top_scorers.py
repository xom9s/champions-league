import requests
import json

def get_top_scorers():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    FOOTBALL_DATA = config['FOOTBALL_DATA']

    uri = 'https://api.football-data.org/v4/competitions/SA/scorers'
    headers = {'X-Auth-Token':FOOTBALL_DATA}

    top_scorers = requests.get(uri, headers=headers)
    for top_scorer in top_scorers.json()['scorers']:
        print(top_scorer)

if __name__ == '__main__':
    get_top_scorers()