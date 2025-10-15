# Articlay - Quick Start Guide

## Installation

```bash
pip install articlay
```

## Configuration

Articlay fetches articles from a GitHub Gist. You need to configure your Gist ID.

### Option 1: Environment Variable (Recommended)

```bash
# Set the environment variable
export ARTICLAY_GIST_ID="your-gist-id-here"

# Or add to your shell profile (~/.bashrc, ~/.zshrc, etc.)
echo 'export ARTICLAY_GIST_ID="your-gist-id-here"' >> ~/.bashrc
source ~/.bashrc
```

### Option 2: Command Line Argument

```bash
articlay --gist-id your-gist-id-here --all
```

### Option 3: Create gist_config.py

Create a file named `gist_config.py` in your working directory:

```python
GIST_ID = "your-gist-id-here"
GIST_FILENAME = "magazine-articles.json"
```

##Usage Examples

### View All Articles

```bash
# With environment variable set
articlay --all --limit 10

# Or with command line argument
articlay --gist-id your-gist-id --all --limit 10
```

### View by Category

```bash
# India news
articlay --india --limit 5

# Technology articles
articlay --codetech --limit 5

# Movie & Entertainment
articlay --movie --limit 5

# Literature
articlay --literature --limit 5

# Fashion & Lifestyle
articlay --foryou --limit 5
```

### Get a Random Article

```bash
articlay random
```

### Available Categories

- `--foryou` - For You (curated articles)
- `--india` - India news
- `--tamilnadu` or `--tn` - Tamil Nadu news
- `--movie` - Movie & Entertainment
- `--literature` or `--lit` - Literature
- `--writing` - Writing & Publishing
- `--reddit` - Reddit highlights
- `--codetech` - Code & Technology
- `--artculture` or `--art` - Art & Culture
- `--others` - Other categories
- `--all` - All articles

## How to Get Your Gist ID

1. **Create a GitHub Gist**:
   - Go to https://gist.github.com/
   - Create a new Gist with a JSON file
   - The Gist ID is in the URL: `https://gist.github.com/username/{GIST_ID}`

2. **Expected Gist Format**:

The Gist should contain a JSON file with articles in this format:

```json
{
  "2025-10-15": {
    "Healthline": [
      {
        "title": "Article Title",
        "link": "https://example.com/article",
        "description": "Article description",
        "pubDate": "2025-10-15",
        "category": "Health"
      }
    ],
    "TechCrunch": [
      {
        "title": "Another Article",
        "link": "https://example.com/article2",
        "category": "Code & Tech"
      }
    ]
  }
}
```

Or a simpler flat structure:

```json
{
  "SourceName": [
    {
      "title": "Article Title",
      "link": "https://example.com",
      "category": "Category"
    }
  ]
}
```

## Private Gists

If your Gist is private, you'll need a GitHub Personal Access Token:

```bash
# Set the token
export GITHUB_TOKEN="your-github-token-here"

# Or pass it via command line
articlay --token your-github-token --all
```

## Common Issues

### "No Gist ID configured"

**Solution**: Set the Gist ID using one of the methods above.

### "No articles found in category"

**Solutions**:
- Check that your Gist has articles with that category
- Try `--all` to see all available articles
- Verify your Gist JSON structure

### "Error fetching articles from Gist"

**Solutions**:
- Check that the Gist ID is correct
- If private, ensure you've set `GITHUB_TOKEN`
- Verify your internet connection
- Check that the Gist contains valid JSON

## Example Workflow

```bash
# 1. Set your Gist ID (one time)
export ARTICLAY_GIST_ID="17c58ca69bfa6f204a353a76f21b7774"

# 2. View all articles
articlay --all --limit 20

# 3. Filter by category
articlay --india --limit 5

# 4. Get a random article
articlay random
```

## Tips

- Use `--limit 0` to show all articles (no limit)
- Add your Gist ID to `~/.bashrc` or `~/.zshrc` for permanent configuration
- Keep your Gist JSON file updated with fresh articles
- Use descriptive categories that match the CLI options

## Version History

- **1.1.3** - Fixed Gist data parsing for nested structures
- **1.1.2** - Added `--gist-id` argument and `ARTICLAY_GIST_ID` env var
- **1.1.1** - Fixed installation issues
- **1.1.0** - Initial PyPI release

## Support

For issues or questions:
- GitHub: https://github.com/pappater/articlay
- PyPI: https://pypi.org/project/articlay/

## License

MIT License - See LICENSE file for details
