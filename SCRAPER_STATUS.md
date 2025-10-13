# Scraper Status Tracking

This document tracks the status of all scrapers in the Articlay project. It helps identify which scrapers are working, which need attention, and which are known to have issues.

## Purpose

When the `daily_gist_job.py` runs, some scrapers may fail due to:
- Website RSS feed changes or removal
- Rate limiting or blocking
- Network connectivity issues
- Website redesigns affecting scraping logic

This document helps track these issues for future resolution.

## Newly Added Scrapers (Pending Production Testing)

These scrapers were added as per requirements and need to be tested in production:

### Movie Scrapers
- `letterboxd_scraper` - Letterboxd (RSS: https://letterboxd.com/journal/rss/)
- `rogerebert_scraper` - RogerEbert.com (RSS: https://www.rogerebert.com/feed)
- `indiewire_scraper` - IndieWire (RSS: https://www.indiewire.com/feed/)
- `filmcompanion_scraper` - Film Companion (RSS: https://www.filmcompanion.in/feed/)

### Literature Scrapers
- `gutenberg_scraper` - Project Gutenberg (RSS: https://www.gutenberg.org/cache/epub/feeds/today.rss)
- `parisreview_scraper` - The Paris Review (RSS: https://www.theparisreview.org/feed)
- `granta_scraper` - Granta (RSS: https://granta.com/feed/)
- `newyorkerbooks_scraper` - The New Yorker Books (RSS: https://www.newyorker.com/feed/books)
- `hinduliteraryreview_scraper` - The Hindu Literary Review (RSS: https://www.thehindu.com/books/literary-review/feeder/default.rss)

### Writing Scrapers
- `substack_scraper` - Substack Reader (RSS: https://substack.com/feed/reader)
- `wattpad_scraper` - Wattpad (RSS: https://www.wattpad.com/home/feed.rss)
- `electricliterature_scraper` - Electric Literature (RSS: https://electricliterature.com/feed/)
- `poets_scraper` - Poets.org (RSS: https://poets.org/rss/poems)

### Reddit Scrapers
- `reddit_scraper.fetch_reddit_writing` - Reddit r/writing

## Known Issues

### To Be Determined

Run the daily job and check logs to identify which scrapers consistently fail. Update this section with:

1. **Scraper Name**: Brief description of the issue
2. **Last Checked**: Date when the issue was verified
3. **Potential Fix**: Ideas for resolution
4. **Status**: Working / Intermittent / Broken / Deprecated

## Known Potential Issues

### Requires Authentication (May Not Work)
- **substack_scraper**: Substack Reader feed likely requires authentication
- **wattpad_scraper**: Wattpad home feed is user-specific and may require login

These scrapers may need alternative RSS feeds or different approaches.

## How to Update This Document

After each run:
1. Check the GitHub Actions logs for failed scrapers
2. Note any scrapers that consistently fail (3+ consecutive runs)
3. Add them to the "Known Issues" section
4. Research potential fixes or alternatives

## Testing Scrapers Manually

To test a specific scraper:

```bash
cd articlay
python -c "
from scrapers.SCRAPER_NAME import fetch_FUNCTION_NAME
articles = fetch_FUNCTION_NAME(limit=5)
print(f'Fetched {len(articles)} articles')
for art in articles[:2]:
    print(f'  - {art[\"title\"]}')
"
```

## Alternative Sources

If a scraper consistently fails, consider these alternatives:
- Look for alternative RSS feeds from the same source
- Find similar sources in the same category
- Check if the website has changed its feed URL
- Consider web scraping if RSS is no longer available (with proper rate limiting)
