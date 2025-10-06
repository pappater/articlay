# Articlay 📰

A tool to aggregate popular magazine articles from Magzter and archive them to GitHub Gist.

## Features

- 🔍 Fetches popular magazines from Magzter
- 📚 Gets latest editions of magazines
- 🎲 Randomly selects articles from different magazines (no duplicates from same magazine)
- ⚙️ Configurable to fetch from top 10, 20, or 30 magazines
- 📝 Lists article titles and links
- 💾 Archives articles to GitHub Gist daily
- 📄 Saves local backup in JSON format

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

## Note

This tool is designed to work with Magzter. Actual scraping implementation may need adjustments based on Magzter's structure and authentication requirements. The current implementation includes a framework that can be extended with proper Magzter API access or web scraping logic.

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.