from components import requests, FOOTBALL_DATA

def get_standings():

    uri = 'https://api.football-data.org/v4/competitions/SA/standings'
    headers = { 'X-Auth-Token': FOOTBALL_DATA}

    standings = requests.get(uri, headers=headers)
    
    return standings.json()['standings']
