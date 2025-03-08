from . import json, requests, FOOTBALL_DATA

def get_top_scorers():

    uri = 'https://api.football-data.org/v4/competitions/SA/scorers'
    headers = {'X-Auth-Token':FOOTBALL_DATA}

    top_scorers = requests.get(uri, headers=headers)
    for top_scorer in top_scorers.json()['scorers']:
        print(top_scorer)

if __name__ == '__main__':
    get_top_scorers()