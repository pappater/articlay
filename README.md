# Articlay 📰

A comprehensive news aggregator that fetches articles from popular magazines and news sources worldwide, including India and Tamil Nadu, and presents them in a beautiful, minimalistic UI.

## Features

- 🌍 **Global Coverage**: Fetches from 30+ news sources including Reuters, Forbes, The Economist, Wired, Nature, and more
- 🇮🇳 **Indian News**: Includes The Hindu, Times of India, Indian Express, NDTV, Hindustan Times
- 🏛️ **Tamil Nadu News**: Features Dinamalar, Dinamani, Daily Thanthi
- 📂 **Categorized Articles**: Organized by World, India, Tamil Nadu, Business, Technology, Science, and Culture
- 🕐 **Daily Automation**: Runs automatically every day at 6:00 AM IST
- 💾 **Gist Storage**: Archives all article data (title, description, link, publish date, category) to GitHub Gist
- 🌐 **GitHub Pages UI**: Beautiful, minimalistic interface to browse articles day-wise
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- 🎯 **One Article Per Source**: Displays one article from each news source per day

## Installation

### Prerequisites

- Python 3.7 or higher
- GitHub Personal Access Token (for Gist archiving)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/pappater/articlay.git
cd articlay
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your GitHub token (for Gist archiving):
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

Or create a `.env` file:
```
GITHUB_TOKEN=your_github_personal_access_token
```

## Usage

### Daily Automation (Recommended)

The repository is configured to automatically fetch articles every day at **6:00 AM IST** via GitHub Actions. The scraped articles are:
1. Stored in a GitHub Gist
2. Displayed on the [live UI](https://pappater.github.io/articlay/)

No manual intervention is required!

### Manual Execution

To manually run the article scraper:

```bash
# Set your GitHub token (required for Gist storage)
export GITHUB_TOKEN="your_github_token_here"

# Run the daily scraper
python daily_gist_job.py
```

This will:
- Fetch 5 articles from each news source
- Store them in the configured GitHub Gist
- Organize them by date and category

### Legacy Magzter Tool

The original `articlay.py` tool for Magzter is still available:

```bash
# Basic usage
python articlay.py

# With options
python articlay.py --magazines 20 --articles 10
```

## Output

The tool generates two types of output:

1. **Console Output**: Displays selected articles with titles, magazine names, and links
2. **JSON File**: Saves articles locally as `articlay-YYYY-MM-DD.json`
3. **GitHub Gist**: Archives articles as markdown to a public Gist (if enabled)

### Example Output

```
📰 Articlay - Magzter Article Aggregator
==================================================

Fetching top 10 popular magazines...
Found 10 magazines

Selecting 5 random articles from different magazines...

📚 Selected Articles:
--------------------------------------------------

1. Magazine 1 - Article 3
   Magazine: Magazine 1
   Link: https://www.magzter.com/magazine-1/article-3

2. Magazine 5 - Article 2
   Magazine: Magazine 5
   Link: https://www.magzter.com/magazine-5/article-2

...

✓ Archived to Gist: https://gist.github.com/...
✓ Articles saved to: articlay-2024-01-15.json
```

## Setup for Your Own Instance

If you want to run Articlay on your own repository:

1. **Fork the repository**

2. **Create a GitHub Gist**
   - Go to https://gist.github.com/
   - Create a new gist with filename `magazine-articles.json`
   - Initialize it with `{}`
   - Copy the Gist ID from the URL

3. **Update Configuration**
   - Edit `gist_config.py` with your Gist ID
   - Edit `docs/index.html` to update the `GIST_ID` constant

4. **Set up GitHub Token**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate a new token with `gist` scope
   - Add it as a repository secret named `GIST_TOKEN`

5. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: main, folder: /docs
   - Save

6. **Enable GitHub Actions**
   - The workflows will run automatically
   - Articles will be fetched daily at 6 AM IST

## Requirements

See `requirements.txt`:
- requests>=2.31.0
- beautifulsoup4>=4.12.0
- lxml>=4.9.0

## Live Demo

Visit the live UI: [https://pappater.github.io/articlay/](https://pappater.github.io/articlay/)

Browse daily articles in a clean, minimalistic interface organized by category.

## News Sources

### World News
- Reuters, Time, The Atlantic, NPR

### Business & Economics
- Forbes, The Economist, Bloomberg

### Technology
- Wired

### Science & Nature
- National Geographic, Scientific American, Popular Science, New Scientist, Nature

### Culture
- The New Yorker, Smithsonian Magazine

### India
- The Hindu, Times of India, Indian Express, NDTV, Hindustan Times

### Tamil Nadu
- Dinamalar, Dinamani, Daily Thanthi

## Automation

Articles are automatically scraped and stored every day at **6:00 AM IST** via GitHub Actions. Non-working scrapers are gracefully skipped.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.