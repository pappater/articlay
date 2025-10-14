import os
import sys
import json
import re
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
    # India News (10 articles each)
    ("thehindu_scraper", "fetch_thehindu_articles", 10),
    ("timesofindia_scraper", "fetch_timesofindia_articles", 10),
    ("indianexpress_scraper", "fetch_indianexpress_articles", 10),
    ("ndtv_scraper", "fetch_ndtv_articles", 10),
    ("hindustantimes_scraper", "fetch_hindustantimes_articles", 10),
    ("zeenews_scraper", "fetch_zeenews_articles", 10),
    ("indiatoday_scraper", "fetch_indiatoday_articles", 10),
    ("ddnews_scraper", "fetch_ddnews_articles", 10),
    ("livemint_scraper", "fetch_livemint_articles", 10),
    ("thewire_scraper", "fetch_thewire_articles", 10),
    ("scroll_scraper", "fetch_scroll_articles", 10),
    ("newindianexpress_scraper", "fetch_newindianexpress_articles", 10),
    ("deccanherald_scraper", "fetch_deccanherald_articles", 10),
    ("outlookindia_scraper", "fetch_outlookindia_articles", 10),
    ("theweek_scraper", "fetch_theweek_articles", 10),
    ("openthemagazine_scraper", "fetch_openthemagazine_articles", 10),
    ("readersdigestindia_scraper", "fetch_readersdigestindia_articles", 10),
    ("caravan_scraper", "fetch_caravan_articles", 10),
    
    # Tamil Nadu News (10 articles each)
    ("dinamalar_scraper", "fetch_dinamalar_articles", 10),
    ("dinamani_scraper", "fetch_dinamani_articles", 10),
    ("thanthi_scraper", "fetch_thanthi_articles", 10),
    
    # Code & Tech (10 articles each)
    ("dev_to_scraper", "fetch_dev_to_articles", 10),
    ("hackernews_scraper", "fetch_hackernews_articles", 10),
    ("css_tricks_scraper", "fetch_css_tricks_articles", 10),
    
    # Movie (10 articles each)
    ("mubi_scraper", "fetch_mubi_articles", 10),
    ("letterboxd_scraper", "fetch_letterboxd_articles", 10),
    ("rogerebert_scraper", "fetch_rogerebert_articles", 10),
    ("indiewire_scraper", "fetch_indiewire_articles", 10),
    ("filmcomment_scraper", "fetch_filmcomment_articles", 10),
    ("criterion_scraper", "fetch_criterion_articles", 10),
    ("filmcompanion_scraper", "fetch_filmcompanion_articles", 10),
    ("variety_scraper", "fetch_variety_articles", 10),
    ("rollingstone_scraper", "fetch_rollingstone_articles", 10),
    ("filmfare_scraper", "fetch_filmfare_articles", 10),
    
    # Literature (10 articles each)
    ("lithub_scraper", "fetch_lithub_articles", 10),
    ("gutenberg_scraper", "fetch_gutenberg_articles", 10),
    ("parisreview_scraper", "fetch_parisreview_articles", 10),
    ("granta_scraper", "fetch_granta_articles", 10),
    ("newyorkerbooks_scraper", "fetch_newyorkerbooks_articles", 10),
    ("bookpage_scraper", "fetch_bookpage_articles", 10),
    ("litreactor_scraper", "fetch_litreactor_articles", 10),
    ("hinduliteraryreview_scraper", "fetch_hinduliteraryreview_articles", 10),
    
    # Writing (10 articles each)
    ("writersdigest_scraper", "fetch_writersdigest_articles", 10),
    ("thewritelife_scraper", "fetch_thewritelife_articles", 10),
    ("medium_scraper", "fetch_medium_articles", 10),
    ("substack_scraper", "fetch_substack_articles", 10),
    ("wattpad_scraper", "fetch_wattpad_articles", 10),
    ("electricliterature_scraper", "fetch_electricliterature_articles", 10),
    ("poets_scraper", "fetch_poets_articles", 10),
    
    # Reddit (10 posts each)
    ("reddit_scraper", "fetch_reddit_worldnews", 10),
    ("reddit_scraper", "fetch_reddit_india", 10),
    ("reddit_scraper", "fetch_reddit_chennai", 10),
    ("reddit_scraper", "fetch_reddit_programming", 10),
    ("reddit_scraper", "fetch_reddit_technology", 10),
    ("reddit_scraper", "fetch_reddit_science", 10),
    ("reddit_scraper", "fetch_reddit_books", 10),
    ("reddit_scraper", "fetch_reddit_movies", 10),
    ("reddit_scraper", "fetch_reddit_writing", 10),
    
    # Art & Culture (10 articles each)
    ("colossal_scraper", "fetch_colossal_articles", 10),
    ("artnet_scraper", "fetch_artnet_articles", 10),
    ("smithsonian_scraper", "fetch_smithsonian_articles", 10),
    ("newyorker_scraper", "fetch_newyorker_articles", 10),
    ("slate_scraper", "fetch_slate_articles", 10),
    ("theatlantic_scraper", "fetch_theatlantic_articles", 10),
    ("exhibit_scraper", "fetch_exhibit_articles", 10),
    
    # AI's Choice - Design Trends (10 articles each)
    ("smashingmagazine_scraper", "fetch_smashingmagazine_articles", 10),
    ("dezeen_scraper", "fetch_dezeen_articles", 10),
    
    # AI's Choice - Minimalist Living (10 articles each)
    ("becomingminimalist_scraper", "fetch_becomingminimalist_articles", 10),
    
    # AI's Choice - Indie Web Projects (10 articles each)
    ("indieweb_scraper", "fetch_indieweb_articles", 10),
    
    # World News (10 articles each)
    ("reuters_scraper", "fetch_reuters_articles", 10),
    ("time_scraper", "fetch_time_articles", 10),
    ("atlantic_scraper", "fetch_atlantic_articles", 10),
    ("npr_scraper", "fetch_npr_articles", 10),
    ("bbc_scraper", "fetch_bbc_articles", 10),
    ("cnn_scraper", "fetch_cnn_articles", 10),
    ("aljazeera_scraper", "fetch_aljazeera_articles", 10),
    ("guardian_scraper", "fetch_guardian_articles", 10),
    ("axios_scraper", "fetch_axios_articles", 10),
    ("usatoday_scraper", "fetch_usatoday_articles", 10),
    ("newsweek_scraper", "fetch_newsweek_articles", 10),
    ("telegraph_scraper", "fetch_telegraph_articles", 10),
    ("independent_scraper", "fetch_independent_articles", 10),
    ("washingtonpost_scraper", "fetch_washingtonpost_articles", 10),
    
    # Business & Economics (10 articles each)
    ("forbes_scraper", "fetch_forbes_articles", 10),
    ("economist_scraper", "fetch_economist_articles", 10),
    ("bloomberg_scraper", "fetch_bloomberg_articles", 10),
    ("wsj_scraper", "fetch_wsj_articles", 10),
    ("businessinsider_scraper", "fetch_businessinsider_articles", 10),
    ("fastcompany_scraper", "fetch_fastcompany_articles", 10),
    ("businessstandard_scraper", "fetch_businessstandard_articles", 10),
    ("businesstoday_scraper", "fetch_businesstoday_articles", 10),
    ("fortuneindia_scraper", "fetch_fortuneindia_articles", 10),
    ("forbesindia_scraper", "fetch_forbesindia_articles", 10),
    
    # Technology (10 articles each)
    ("wired_scraper", "fetch_wired_articles", 10),
    ("theverge_scraper", "fetch_theverge_articles", 10),
    ("arstechnica_scraper", "fetch_arstechnica_articles", 10),
    ("engadget_scraper", "fetch_engadget_articles", 10),
    ("mashable_scraper", "fetch_mashable_articles", 10),
    ("techcrunch_scraper", "fetch_techcrunch_articles", 10),
    ("medium_scraper", "fetch_medium_articles", 10),
    ("t3india_scraper", "fetch_t3india_articles", 10),
    ("pcquest_scraper", "fetch_pcquest_articles", 10),
    ("electronicsforyou_scraper", "fetch_electronicsforyou_articles", 10),
    ("opensourceforyou_scraper", "fetch_opensourceforyou_articles", 10),
    
    # Science & Nature (10 articles each)
    ("natgeo_scraper", "fetch_natgeo_articles", 10),
    ("scientificamerican_scraper", "fetch_scientificamerican_articles", 10),
    ("popsci_scraper", "fetch_popsci_articles", 10),
    ("newscientist_scraper", "fetch_newscientist_articles", 10),
    ("nature_scraper", "fetch_nature_articles", 10),
    
    # Space & Astronomy (10 articles each)
    ("space_scraper", "fetch_space_articles", 10),
    
    # Culture & Arts (10 articles each)
    ("newyorker_scraper", "fetch_newyorker_articles", 10),
    ("smithsonian_scraper", "fetch_smithsonian_articles", 10),
    ("artnet_scraper", "fetch_artnet_articles", 10),
    ("slate_scraper", "fetch_slate_articles", 10),
    ("theatlantic_scraper", "fetch_theatlantic_articles", 10),
    
    # Sports (10 articles each)
    ("espn_scraper", "fetch_espn_articles", 10),
    
    # Health (10 articles each)
    ("healthline_scraper", "fetch_healthline_articles", 10),
    
    # Environment (10 articles each)
    ("treehugger_scraper", "fetch_treehugger_articles", 10),
    
    # Politics (10 articles each)
    ("politico_scraper", "fetch_politico_articles", 10),
    ("fivethirtyeight_scraper", "fetch_fivethirtyeight_articles", 10),
    
    # Entertainment (10 articles each)
    ("variety_scraper", "fetch_variety_articles", 10),
    ("rollingstone_scraper", "fetch_rollingstone_articles", 10),
    
    # Fashion & Lifestyle (10 articles each)
    ("vogue_scraper", "fetch_vogue_articles", 10),
    ("gq_scraper", "fetch_gq_articles", 10),
    ("vogueindia_scraper", "fetch_vogueindia_articles", 10),
    ("feminaindia_scraper", "fetch_feminaindia_articles", 10),
    ("cosmopolitanindia_scraper", "fetch_cosmopolitanindia_articles", 10),
    ("gqindia_scraper", "fetch_gqindia_articles", 10),
    ("graziaindia_scraper", "fetch_graziaindia_articles", 10),
    ("harpersbazaar_scraper", "fetch_harpersbazaar_articles", 10),
    ("elle_scraper", "fetch_elle_articles", 10),
    
    # Food (10 articles each)
    ("bonappetit_scraper", "fetch_bonappetit_articles", 10),
    ("bakeryreview_scraper", "fetch_bakeryreview_articles", 10),
    
    # Education (10 articles each)
    ("edweek_scraper", "fetch_edweek_articles", 10),
    ("mathematicstoday_scraper", "fetch_mathematicstoday_articles", 10),
    
    # Travel (10 articles each)
    ("outlooktraveller_scraper", "fetch_outlooktraveller_articles", 10),
    ("businesstravellerindia_scraper", "fetch_businesstravellerindia_articles", 10),
    
    # Home & Design (10 articles each)
    ("goodhomesindia_scraper", "fetch_goodhomesindia_articles", 10),
    ("elledecor_scraper", "fetch_elledecor_articles", 10),
    
    # Architecture (10 articles each)
    ("architectandinteriors_scraper", "fetch_architectandinteriors_articles", 10),
    ("admagazine_scraper", "fetch_admagazine_articles", 10),
    
    # Auto (10 articles each)
    ("topgearindia_scraper", "fetch_topgearindia_articles", 10),
    ("autocar_scraper", "fetch_autocar_articles", 10),
    ("bikeindia_scraper", "fetch_bikeindia_articles", 10),
    ("carindia_scraper", "fetch_carindia_articles", 10),
    
    # Health & Fitness (10 articles each)
    ("womensfitnessindia_scraper", "fetch_womensfitnessindia_articles", 10),
    
    # Photography (10 articles each)
    ("smartphotography_scraper", "fetch_smartphotography_articles", 10),
    
    # Men's Lifestyle (10 articles each)
    ("mansworld_scraper", "fetch_mansworld_articles", 10),
    
    # Wikipedia & Special Content (1 article each - special content)
    ("wikipedia_scraper", "fetch_wikipedia_article_of_day", 1),
    ("wikipedia_scraper", "fetch_wikipedia_image_of_day", 1),
    ("wikipedia_scraper", "fetch_random_wikipedia_article", 1),
    ("wikipedia_scraper", "fetch_wikipedia_quote_of_day", 1),
    ("wikipedia_scraper", "fetch_on_this_day", 1),
    
    # Quotes & Inspiration (1 article each - special content)
    ("quotes_scraper", "fetch_quote_of_day", 1),
    ("quotes_scraper", "fetch_zen_quote", 1),
]

def strip_images_from_description(description):
    """Remove image tags and URLs from description, and strip remaining HTML."""
    if not description:
        return description
    
    # Remove HTML img tags
    description = re.sub(r'<img[^>]*>', '', description)
    # Remove markdown image syntax ![alt](url)
    description = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', r'\1', description)
    # Remove standalone image URLs (common patterns)
    description = re.sub(r'https?://[^\s]*\.(jpg|jpeg|png|gif|webp)', '', description, flags=re.IGNORECASE)
    
    # Strip all remaining HTML tags for text-only output (efficient regex-based approach)
    description = re.sub(r'<[^>]*>', '', description)
    
    # Clean up extra whitespace
    description = ' '.join(description.split())
    
    return description

# Premium/Featured sources that should be flagged
PREMIUM_SOURCES = {
    'wsj', 'wall street journal', 'wallstreetjournal',
    'time',
    'washingtonpost', 'washington post', 'the washington post',
    'indiatoday', 'india today',
    'vogueindia', 'vogue india',
    'businessstandard', 'business standard',
    'outlookindia', 'outlook',
    'feminaindia', 'femina india',
    'cosmopolitanindia', 'cosmopolitan india',
    'theweek', 'the week',
    'openthemagazine', 'open',
    'filmfare',
    'businesstoday', 'business today',
    'gqindia', 'gq india',
    'readersdigestindia', 'readers digest india',
    'graziaindia', 'grazia india',
    'exhibit',
    'outlooktraveller', 'outlook traveller',
    'mansworld',
    'goodhomesindia', 'goodhomes india',
    'elledecor', 'elle decor india',
    'architectandinteriors', 'architect and interiors india',
    'businesstravellerindia', 'business traveller india',
    'fortuneindia', 'fortune india',
    'livemint', 'mint',
    'hindustantimes', 'hindustan times',
    'forbesindia', 'forbes india',
    't3india', 't3 india',
    'caravan', 'the caravan',
    'admagazine', 'ad architectural digest',
    'topgearindia', 'top gear india',
    'harpersbazaar', 'bazaar',
    'elle',
    'pcquest', 'pc quest',
    'electronicsforyou', 'electronics for you',
    'autocar',
    'opensourceforyou', 'open source for you',
    'rollingstone',
    'bakeryreview', 'bakery review',
    'mathematicstoday', 'mathematics today',
    'bikeindia', 'bike india',
    'carindia', 'car india',
    'womenfitnessindia', 'women fitness india',
    'smartphotography', 'smart photography'
}

def is_premium_source(source_name):
    """Check if a source should be flagged as premium."""
    source_normalized = source_name.lower().strip().replace(' ', '').replace('-', '')
    return any(premium.replace(' ', '').replace('-', '') in source_normalized 
               for premium in PREMIUM_SOURCES)

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
                        elif "programming" in func:
                            source_name = "Reddit Programming"
                        elif "technology" in func:
                            source_name = "Reddit Technology"
                        elif "science" in func:
                            source_name = "Reddit Science"
                        else:
                            source_name = func.replace('fetch_reddit_', 'Reddit ').title()
                    else:
                        source_name = module.replace('_scraper', '').capitalize()
                    
                    # Add premium flag to articles if source is premium
                    if is_premium_source(source_name):
                        for article in unique_articles:
                            article['premium'] = True
                    
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
    
    # Only keep current date's articles (no archiving)
    print("\nPreparing Gist data for current date only...")
    current_data = {date_str: all_articles}
    
    print("\nUpdating Gist...")
    update_gist(current_data, github_token)

if __name__ == "__main__":
    main()
