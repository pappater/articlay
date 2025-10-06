import requests
from bs4 import BeautifulSoup
from typing import List, Dict

WIRED_RSS = "https://www.wired.com/feed/rss"

def fetch_wired_articles(limit: int = 5) -> List[Dict]:
    """Fetch latest articles from Wired RSS feed."""
    articles = []
    try:
        resp = requests.get(WIRED_RSS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, features="xml")
        items = soup.find_all('item')[:limit]
        for item in items:
            title = item.title.text.strip()
            link = item.link.text.strip()
            articles.append({"title": title, "link": link})
    except Exception as e:
        print(f"Error fetching Wired articles: {e}")
    return articles

if __name__ == "__main__":
    for art in fetch_wired_articles():
        print(f"{art['title']}\n{art['link']}\n")
