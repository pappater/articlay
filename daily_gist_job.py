import os
import sys
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Add scrapers directory to sys.path
sys.path.append(str(Path(__file__).parent / "scrapers"))

import requests
from gist_config import GIST_ID, GIST_FILENAME

# Import all scraper functions
def import_scraper(module_name, func_name):
    mod = __import__(module_name)
    return getattr(mod, func_name)

SCRAPERS = [
    # World News
    ("reuters_scraper", "fetch_reuters_articles"),
    ("time_scraper", "fetch_time_articles"),
    ("atlantic_scraper", "fetch_atlantic_articles"),
    ("npr_scraper", "fetch_npr_articles"),
    ("bbc_scraper", "fetch_bbc_articles"),
    ("cnn_scraper", "fetch_cnn_articles"),
    ("aljazeera_scraper", "fetch_aljazeera_articles"),
    
    # Business & Economics
    ("forbes_scraper", "fetch_forbes_articles"),
    ("economist_scraper", "fetch_economist_articles"),
    ("bloomberg_scraper", "fetch_bloomberg_articles"),
    
    # Technology
    ("wired_scraper", "fetch_wired_articles"),
    
    # Science & Nature
    ("natgeo_scraper", "fetch_natgeo_articles"),
    ("scientificamerican_scraper", "fetch_scientificamerican_articles"),
    ("popsci_scraper", "fetch_popsci_articles"),
    ("newscientist_scraper", "fetch_newscientist_articles"),
    ("nature_scraper", "fetch_nature_articles"),
    
    # Culture
    ("newyorker_scraper", "fetch_newyorker_articles"),
    ("smithsonian_scraper", "fetch_smithsonian_articles"),
    
    # India News
    ("thehindu_scraper", "fetch_thehindu_articles"),
    ("timesofindia_scraper", "fetch_timesofindia_articles"),
    ("indianexpress_scraper", "fetch_indianexpress_articles"),
    ("ndtv_scraper", "fetch_ndtv_articles"),
    ("hindustantimes_scraper", "fetch_hindustantimes_articles"),
    ("zeenews_scraper", "fetch_zeenews_articles"),
    ("indiatoday_scraper", "fetch_indiatoday_articles"),
    ("ddnews_scraper", "fetch_ddnews_articles"),
    
    # Tamil Nadu News
    ("dinamalar_scraper", "fetch_dinamalar_articles"),
    ("dinamani_scraper", "fetch_dinamani_articles"),
    ("thanthi_scraper", "fetch_thanthi_articles"),
    
    # Wikipedia & Special Content
    ("wikipedia_scraper", "fetch_wikipedia_article_of_day"),
    ("wikipedia_scraper", "fetch_wikipedia_image_of_day"),
    ("wikipedia_scraper", "fetch_random_wikipedia_article"),
    ("wikipedia_scraper", "fetch_wikipedia_quote_of_day"),
    ("wikipedia_scraper", "fetch_on_this_day"),
    
    # Quotes & Inspiration
    ("quotes_scraper", "fetch_quote_of_day"),
    ("quotes_scraper", "fetch_zen_quote"),
]

def run_all_scrapers():
    all_articles = {}
    successful = 0
    failed = 0
    seen_titles = set()  # Track seen article titles for deduplication
    
    for module, func in SCRAPERS:
        try:
            fetch_func = import_scraper(module, func)
            articles = fetch_func()
            
            # Only store if we got articles
            if articles and len(articles) > 0:
                # Deduplicate articles by title
                unique_articles = []
                for article in articles:
                    title_key = article.get('title', '').lower().strip()
                    if title_key and title_key not in seen_titles:
                        unique_articles.append(article)
                        seen_titles.add(title_key)
                
                if unique_articles:
                    # Create a unique source name using both module and function
                    if module == "wikipedia_scraper":
                        # Special handling for Wikipedia scrapers
                        source_name = func.replace('fetch_', '').replace('_', ' ').title()
                    else:
                        source_name = module.replace('_scraper', '').capitalize()
                    
                    all_articles[source_name] = unique_articles
                    successful += 1
                    print(f"✓ {source_name}: {len(unique_articles)} articles")
                else:
                    print(f"✓ {module}: All articles were duplicates")
            else:
                failed += 1
                print(f"✗ {module}: No articles returned")
        except Exception as e:
            failed += 1
            print(f"✗ {module}: Error - {str(e)[:100]}")
    
    print(f"\nSummary: {successful} sources successful, {failed} sources failed")
    return all_articles

def fetch_existing_gist(gist_id, filename, github_token):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {github_token}"}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        files = resp.json().get("files", {})
        if filename in files:
            content = files[filename]["content"]
            try:
                return json.loads(content)
            except Exception:
                return {}
    return {}

def update_gist(data, github_token):
    url = f"https://api.github.com/gists/{GIST_ID}"
    headers = {"Authorization": f"token {github_token}"}
    payload = {
        "files": {
            GIST_FILENAME: {"content": json.dumps(data, indent=2)}
        }
    }
    resp = requests.patch(url, headers=headers, json=payload)
    if resp.status_code == 200:
        gist_url = resp.json()["html_url"]
        print(f"Gist updated: {gist_url}")
        return gist_url
    else:
        print(f"Failed to update gist: {resp.text}")
        return None

def main():
    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GITHUB_TOKEN not set in environment.")
        return
    
    # Use IST timezone (UTC+5:30)
    ist = timezone(timedelta(hours=5, minutes=30))
    date_str = datetime.now(ist).strftime("%Y-%m-%d")
    
    print(f"Starting article scraping for {date_str} IST")
    print("=" * 60)
    
    all_articles = run_all_scrapers()
    
    if not all_articles:
        print("\nNo articles fetched. Exiting without updating Gist.")
        return
    
    # Fetch existing data
    print("\nFetching existing Gist data...")
    existing = fetch_existing_gist(GIST_ID, GIST_FILENAME, github_token)
    existing[date_str] = all_articles
    
    print("\nUpdating Gist...")
    update_gist(existing, github_token)

if __name__ == "__main__":
    main()
