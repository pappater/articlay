import os
import sys
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Add scrapers directory to sys.path
sys.path.append(str(Path(__file__).parent / "scrapers"))

import requests
from bs4 import BeautifulSoup
from gist_config import GIST_ID, GIST_FILENAME

# Import all scraper functions
def import_scraper(module_name, func_name):
    mod = __import__(module_name)
    return getattr(mod, func_name)

SCRAPERS = [
    # India News (5 articles each)
    ("thehindu_scraper", "fetch_thehindu_articles", 5),
    ("timesofindia_scraper", "fetch_timesofindia_articles", 5),
    ("indianexpress_scraper", "fetch_indianexpress_articles", 5),
    ("ndtv_scraper", "fetch_ndtv_articles", 5),
    ("hindustantimes_scraper", "fetch_hindustantimes_articles", 5),
    ("zeenews_scraper", "fetch_zeenews_articles", 5),
    ("indiatoday_scraper", "fetch_indiatoday_articles", 5),
    ("ddnews_scraper", "fetch_ddnews_articles", 5),
    ("livemint_scraper", "fetch_livemint_articles", 5),
    ("thewire_scraper", "fetch_thewire_articles", 5),
    ("scroll_scraper", "fetch_scroll_articles", 5),
    ("newindianexpress_scraper", "fetch_newindianexpress_articles", 5),
    
    # Tamil Nadu News (5 articles each)
    ("dinamalar_scraper", "fetch_dinamalar_articles", 5),
    ("dinamani_scraper", "fetch_dinamani_articles", 5),
    ("thanthi_scraper", "fetch_thanthi_articles", 5),
    
    # Code & Tech (3 articles total)
    ("dev_to_scraper", "fetch_dev_to_articles", 1),
    ("hackernews_scraper", "fetch_hackernews_articles", 1),
    ("css_tricks_scraper", "fetch_css_tricks_articles", 1),
    
    # Literature (3 articles total)
    ("lithub_scraper", "fetch_lithub_articles", 1),
    ("bookpage_scraper", "fetch_bookpage_articles", 1),
    ("litreactor_scraper", "fetch_litreactor_articles", 1),
    
    # Movie (3 articles total)
    ("mubi_scraper", "fetch_mubi_articles", 1),
    ("filmcomment_scraper", "fetch_filmcomment_articles", 1),
    ("criterion_scraper", "fetch_criterion_articles", 1),
    
    # Writing (2 articles total)
    ("writersdigest_scraper", "fetch_writersdigest_articles", 1),
    ("thewritelife_scraper", "fetch_thewritelife_articles", 1),
    
    # Reddit (5 posts each)
    ("reddit_scraper", "fetch_reddit_worldnews", 5),
    ("reddit_scraper", "fetch_reddit_india", 5),
    ("reddit_scraper", "fetch_reddit_chennai", 5),
    
    # AI's Choice - Art & Photography
    ("colossal_scraper", "fetch_colossal_articles", 1),
    
    # AI's Choice - Design Trends
    ("smashingmagazine_scraper", "fetch_smashingmagazine_articles", 1),
    ("dezeen_scraper", "fetch_dezeen_articles", 1),
    
    # AI's Choice - Minimalist Living
    ("becomingminimalist_scraper", "fetch_becomingminimalist_articles", 1),
    
    # AI's Choice - Indie Web Projects
    ("indieweb_scraper", "fetch_indieweb_articles", 1),
    
    # World News (1 article each)
    ("reuters_scraper", "fetch_reuters_articles", 1),
    ("time_scraper", "fetch_time_articles", 1),
    ("atlantic_scraper", "fetch_atlantic_articles", 1),
    ("npr_scraper", "fetch_npr_articles", 1),
    ("bbc_scraper", "fetch_bbc_articles", 1),
    ("cnn_scraper", "fetch_cnn_articles", 1),
    ("aljazeera_scraper", "fetch_aljazeera_articles", 1),
    ("guardian_scraper", "fetch_guardian_articles", 1),
    ("axios_scraper", "fetch_axios_articles", 1),
    
    # Business & Economics (1 article each)
    ("forbes_scraper", "fetch_forbes_articles", 1),
    ("economist_scraper", "fetch_economist_articles", 1),
    ("bloomberg_scraper", "fetch_bloomberg_articles", 1),
    ("wsj_scraper", "fetch_wsj_articles", 1),
    
    # Technology (1 article each)
    ("wired_scraper", "fetch_wired_articles", 1),
    ("theverge_scraper", "fetch_theverge_articles", 1),
    ("arstechnica_scraper", "fetch_arstechnica_articles", 1),
    ("engadget_scraper", "fetch_engadget_articles", 1),
    ("mashable_scraper", "fetch_mashable_articles", 1),
    
    # Science & Nature (1 article each)
    ("natgeo_scraper", "fetch_natgeo_articles", 1),
    ("scientificamerican_scraper", "fetch_scientificamerican_articles", 1),
    ("popsci_scraper", "fetch_popsci_articles", 1),
    ("newscientist_scraper", "fetch_newscientist_articles", 1),
    ("nature_scraper", "fetch_nature_articles", 1),
    
    # Space & Astronomy (1 article each)
    ("space_scraper", "fetch_space_articles", 1),
    
    # Culture & Arts (1 article each)
    ("newyorker_scraper", "fetch_newyorker_articles", 1),
    ("smithsonian_scraper", "fetch_smithsonian_articles", 1),
    ("artnet_scraper", "fetch_artnet_articles", 1),
    
    # Sports (1 article each)
    ("espn_scraper", "fetch_espn_articles", 1),
    
    # Health (1 article each)
    ("healthline_scraper", "fetch_healthline_articles", 1),
    
    # Environment (1 article each)
    ("treehugger_scraper", "fetch_treehugger_articles", 1),
    
    # Politics (1 article each)
    ("politico_scraper", "fetch_politico_articles", 1),
    
    # Entertainment (1 article each)
    ("variety_scraper", "fetch_variety_articles", 1),
    ("rollingstone_scraper", "fetch_rollingstone_articles", 1),
    
    # Fashion & Lifestyle (1 article each)
    ("vogue_scraper", "fetch_vogue_articles", 1),
    ("gq_scraper", "fetch_gq_articles", 1),
    
    # Food (1 article each)
    ("bonappetit_scraper", "fetch_bonappetit_articles", 1),
    
    # Education (1 article each)
    ("edweek_scraper", "fetch_edweek_articles", 1),
    
    # Wikipedia & Special Content (1 article each)
    ("wikipedia_scraper", "fetch_wikipedia_article_of_day", 1),
    ("wikipedia_scraper", "fetch_wikipedia_image_of_day", 1),
    ("wikipedia_scraper", "fetch_random_wikipedia_article", 1),
    ("wikipedia_scraper", "fetch_wikipedia_quote_of_day", 1),
    ("wikipedia_scraper", "fetch_on_this_day", 1),
    
    # Quotes & Inspiration (1 article each)
    ("quotes_scraper", "fetch_quote_of_day", 1),
    ("quotes_scraper", "fetch_zen_quote", 1),
]

def strip_images_from_description(description):
    """Remove image tags and URLs from description."""
    if not description:
        return description
    
    # Remove HTML img tags
    description = re.sub(r'<img[^>]*>', '', description)
    # Remove markdown image syntax ![alt](url)
    description = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', r'\1', description)
    # Remove standalone image URLs (common patterns)
    description = re.sub(r'https?://[^\s]*\.(jpg|jpeg|png|gif|webp)', '', description, flags=re.IGNORECASE)
    
    # Clean up extra whitespace
    description = ' '.join(description.split())
    
    return description

def run_all_scrapers():
    all_articles = {}
    successful = 0
    failed = 0
    seen_titles = set()  # Track seen article titles for deduplication
    
    for scraper_info in SCRAPERS:
        module, func = scraper_info[0], scraper_info[1]
        limit = scraper_info[2] if len(scraper_info) > 2 else 1
        
        try:
            fetch_func = import_scraper(module, func)
            articles = fetch_func(limit=limit)
            
            # Only store if we got articles
            if articles and len(articles) > 0:
                # Deduplicate articles by title
                unique_articles = []
                for article in articles:
                    title_key = article.get('title', '').lower().strip()
                    if title_key and title_key not in seen_titles:
                        # Strip images from description
                        if 'description' in article:
                            article['description'] = strip_images_from_description(article['description'])
                        
                        unique_articles.append(article)
                        seen_titles.add(title_key)
                
                if unique_articles:
                    # Create a unique source name using both module and function
                    if module == "wikipedia_scraper":
                        # Special handling for Wikipedia scrapers
                        source_name = func.replace('fetch_', '').replace('_', ' ').title()
                    elif module == "reddit_scraper":
                        # Special handling for Reddit scrapers
                        if "worldnews" in func:
                            source_name = "Reddit Worldnews"
                        elif "india" in func:
                            source_name = "Reddit India"
                        elif "chennai" in func:
                            source_name = "Reddit Chennai"
                        else:
                            source_name = func.replace('fetch_reddit_', 'Reddit ').title()
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
