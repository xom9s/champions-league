from . import requests, json, NEWS_API_KEY

try:
    uri = f'https://newsapi.org/v2/everything?q=PremierLeague&from=2025-02-12&language=en&sortBy=popularity&apiKey={NEWS_API_KEY}'
    news = requests.get(uri)
    news.raise_for_status()
    for article in news.json()['articles']:
        print(f"Title:{article['title']}, URL:{article['url']}")
        
except requests.exceptions.RequestException as e:
    print (f"An error occured {e}")