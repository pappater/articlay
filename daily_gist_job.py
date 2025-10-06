import os
import sys
import json
from datetime import datetime
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
    ("reuters_scraper", "fetch_reuters_articles"),
    ("forbes_scraper", "fetch_forbes_articles"),
    ("wired_scraper", "fetch_wired_articles"),
    ("time_scraper", "fetch_time_articles"),
    ("natgeo_scraper", "fetch_natgeo_articles"),
    ("newyorker_scraper", "fetch_newyorker_articles"),
    ("atlantic_scraper", "fetch_atlantic_articles"),
    ("npr_scraper", "fetch_npr_articles"),
    ("smithsonian_scraper", "fetch_smithsonian_articles"),
    ("scientificamerican_scraper", "fetch_scientificamerican_articles"),
    ("popsci_scraper", "fetch_popsci_articles"),
    ("newscientist_scraper", "fetch_newscientist_articles"),
    ("economist_scraper", "fetch_economist_articles"),
    ("bloomberg_scraper", "fetch_bloomberg_articles"),
    ("nature_scraper", "fetch_nature_articles"),
]

def run_all_scrapers():
    all_articles = {}
    for module, func in SCRAPERS:
        try:
            fetch_func = import_scraper(module, func)
            articles = fetch_func()
            all_articles[module.replace('_scraper','').capitalize()] = articles
        except Exception as e:
            print(f"Error running {module}: {e}")
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
    date_str = datetime.now().strftime("%Y-%m-%d")
    all_articles = run_all_scrapers()
    # Fetch existing data
    existing = fetch_existing_gist(GIST_ID, GIST_FILENAME, github_token)
    existing[date_str] = all_articles
    update_gist(existing, github_token)

if __name__ == "__main__":
    main()
