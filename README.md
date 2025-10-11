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

### Basic Usage

Fetch 5 random articles from top 10 magazines:
```bash
python articlay.py
```

### Advanced Options

Fetch from top 20 magazines:
```bash
python articlay.py --magazines 20
```

Fetch 10 articles instead of 5:
```bash
python articlay.py --articles 10
```

Fetch from top 30 magazines, 7 articles, skip Gist archiving:
```bash
python articlay.py --magazines 30 --articles 7 --no-archive
```

Pass GitHub token directly:
```bash
python articlay.py --token YOUR_GITHUB_TOKEN
```

### Command Line Arguments

- `--magazines, -m`: Number of top magazines to consider (choices: 10, 20, 30, default: 10)
- `--articles, -a`: Number of articles to select (default: 5)
- `--no-archive`: Skip archiving to GitHub Gist
- `--token, -t`: GitHub personal access token

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

## GitHub Gist Archiving

To use Gist archiving, you need a GitHub Personal Access Token:

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate a new token with `gist` scope
3. Set the token as an environment variable or pass it via `--token`

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