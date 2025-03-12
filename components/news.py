from . import requests, json, NEWS_API_KEY

def get_news():
    news_urls = []
    try:

        uri = f'https://newsapi.org/v2/everything?q=Serie-a&from=2025-02-12&language=en&sortBy=popularity&apiKey={NEWS_API_KEY}'
        news = requests.get(uri)
        news.raise_for_status()
        for article in news.json()['articles']:
            news_urls.append(article['url'])
        return news_urls
            
    except requests.exceptions.RequestException as e:
        print (f"An error occured {e}")

if __name__ == "__main__":
    get_news()