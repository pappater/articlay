import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def fetch_wikipedia_article_of_day() -> List[Dict]:
    """Fetch Wikipedia's Article of the Day (Featured Article)."""
    articles = []
    try:
        url = "https://en.wikipedia.org/api/rest_v1/feed/featured/2024/01/01"
        # Get today's featured article
        response = requests.get("https://en.wikipedia.org/w/api.php", params={
            "action": "query",
            "format": "json",
            "prop": "extracts|pageimages",
            "generator": "search",
            "gsrsearch": "intitle:Main Page",
            "exintro": True,
            "explaintext": True,
            "piprop": "thumbnail",
            "pithumbsize": 400
        }, timeout=10)
        
        # Alternative: Get today's featured article from the main page
        main_page = requests.get("https://en.wikipedia.org/wiki/Main_Page", timeout=10)
        soup = BeautifulSoup(main_page.content, 'html.parser')
        
        # Find the featured article section
        featured = soup.find('div', {'id': 'mp-tfa'})
        if featured:
            title_elem = featured.find('b')
            title = title_elem.text if title_elem else "Featured Article"
            
            # Get the article link
            link_elem = featured.find('a', href=True)
            article_link = f"https://en.wikipedia.org{link_elem['href']}" if link_elem else "https://en.wikipedia.org"
            
            # Get the content
            paragraphs = featured.find_all('p')
            content = ' '.join([p.get_text() for p in paragraphs])
            
            articles.append({
                "title": f"Wikipedia Article of the Day: {title}",
                "link": article_link,
                "description": content[:500] + "..." if len(content) > 500 else content,
                "content": content,
                "pubDate": "",
                "category": "Wikipedia"
            })
    except Exception as e:
        print(f"Error fetching Wikipedia Article of the Day: {e}")
    return articles

def fetch_wikipedia_image_of_day() -> List[Dict]:
    """Fetch Wikipedia's Picture of the Day."""
    articles = []
    try:
        # Get Wikimedia Commons Picture of the Day
        url = "https://commons.wikimedia.org/wiki/Template:Potd"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the image
        img_elem = soup.find('div', {'class': 'potd'})
        if not img_elem:
            img_elem = soup.find('img')
        
        if img_elem and img_elem.name == 'img':
            img_url = img_elem.get('src', '')
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
        else:
            img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Wikipedia%27s_W.svg/200px-Wikipedia%27s_W.svg.png"
        
        # Get description
        desc_elem = soup.find('div', {'class': 'description'})
        description = desc_elem.get_text().strip() if desc_elem else "Wikipedia Picture of the Day"
        
        articles.append({
            "title": "Wikipedia Picture of the Day",
            "link": url,
            "description": description,
            "image_url": img_url,
            "pubDate": "",
            "category": "Wikipedia"
        })
    except Exception as e:
        print(f"Error fetching Wikipedia Picture of the Day: {e}")
    return articles

def fetch_random_wikipedia_article() -> List[Dict]:
    """Fetch a random Wikipedia article."""
    articles = []
    try:
        response = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/summary", timeout=10)
        data = response.json()
        
        articles.append({
            "title": f"Random Wikipedia Article: {data.get('title', 'Unknown')}",
            "link": data.get('content_urls', {}).get('desktop', {}).get('page', 'https://en.wikipedia.org'),
            "description": data.get('extract', ''),
            "pubDate": "",
            "category": "Wikipedia"
        })
    except Exception as e:
        print(f"Error fetching random Wikipedia article: {e}")
    return articles

def fetch_wikipedia_quote_of_day() -> List[Dict]:
    """Fetch quote of the day from Wikiquote."""
    articles = []
    try:
        # Try to get quote from Wikiquote's main page
        url = "https://en.wikiquote.org/wiki/Main_Page"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the quote of the day
        qotd = soup.find('div', {'id': 'mf-qotd'})
        if not qotd:
            qotd = soup.find('table', {'class': 'qotd'})
        
        if qotd:
            quote_text = qotd.get_text().strip()
            # Clean up the text
            quote_text = ' '.join(quote_text.split())
            
            articles.append({
                "title": "Wikiquote Quote of the Day",
                "link": url,
                "description": quote_text[:300] + "..." if len(quote_text) > 300 else quote_text,
                "content": quote_text,
                "pubDate": "",
                "category": "Wikipedia"
            })
    except Exception as e:
        print(f"Error fetching Wikiquote Quote of the Day: {e}")
    return articles

def fetch_on_this_day() -> List[Dict]:
    """Fetch 'On This Day' events from Wikipedia."""
    articles = []
    try:
        from datetime import datetime
        today = datetime.now()
        month_name = today.strftime("%B")
        day = today.day
        
        url = f"https://en.wikipedia.org/wiki/{month_name}_{day}"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the events section
        events_section = soup.find('span', {'id': 'Events'})
        if events_section:
            events_list = events_section.find_next('ul')
            if events_list:
                events = events_list.find_all('li')[:5]  # Get first 5 events
                events_text = '\n'.join([f"• {event.get_text().strip()}" for event in events])
                
                articles.append({
                    "title": f"On This Day in History ({month_name} {day})",
                    "link": url,
                    "description": events_text,
                    "content": events_text,
                    "pubDate": "",
                    "category": "Wikipedia"
                })
    except Exception as e:
        print(f"Error fetching On This Day: {e}")
    return articles

if __name__ == "__main__":
    print("Wikipedia Article of the Day:")
    for art in fetch_wikipedia_article_of_day():
        print(f"{art['title']}\n{art['link']}\n")
    
    print("\nWikipedia Picture of the Day:")
    for art in fetch_wikipedia_image_of_day():
        print(f"{art['title']}\n{art['link']}\n")
    
    print("\nRandom Wikipedia Article:")
    for art in fetch_random_wikipedia_article():
        print(f"{art['title']}\n{art['link']}\n")
    
    print("\nWikiquote Quote of the Day:")
    for art in fetch_wikipedia_quote_of_day():
        print(f"{art['title']}\n{art['link']}\n")
    
    print("\nOn This Day:")
    for art in fetch_on_this_day():
        print(f"{art['title']}\n{art['link']}\n")
