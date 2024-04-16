import feedparser
import requests

class CoinTelegraphRssReader:
  def __init__(self):
    self.BASE_URL = "https://cointelegraph.com/rss/tag/bitcoin"
    self.headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    
  def get_news(self):
    result = requests.get(self.BASE_URL, headers=self.headers).content    
    feed = feedparser.parse(result)
    
    articles = []

    for entry in feed.entries:
        article = {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary
        }
        articles.append(article)
    
    return articles