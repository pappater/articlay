import requests
from bs4 import BeautifulSoup
from typing import List, Dict

NEWSCIENTIST_RSS = "https://www.newscientist.com/feed/home/"

def fetch_newscientist_articles(limit: int = 5) -> List[Dict]:
    articles = []
    try:
        resp = requests.get(NEWSCIENTIST_RSS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, features="xml")
        items = soup.find_all('item')[:limit]
        for item in items:
            title = item.title.text.strip()
            link = item.link.text.strip()
            articles.append({"title": title, "link": link})
    except Exception as e:
        print(f"Error fetching New Scientist articles: {e}")
    return articles

if __name__ == "__main__":
    for art in fetch_newscientist_articles():
        print(f"{art['title']}\n{art['link']}\n")
