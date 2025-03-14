from typing import Any, Dict, List, Optional
from components import FOOTBALL_DATA
import requests

FOOTBALL_API_URI = 'https://api.football-data.org/v4/competitions/SA/standings'

def get_standings() -> Optional[List[Dict[str, Any]]]:

    headers = { 'X-Auth-Token': FOOTBALL_DATA}
    try:
        standings = requests.get(FOOTBALL_API_URI, headers=headers)
        standings.raise_for_status()
        data = standings.json()
        return data.get('standings', [])
    
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching standings {e}")
        return []
