# Articlay UI

This is the GitHub Pages UI for Articlay. It displays daily news and articles in a minimalistic, easy-to-read format.

## Features

- **Today's Stories**: Displays articles scraped on the current day (IST timezone)
- **Categorized View**: Articles organized by category (India, Tamil Nadu, World, Business, Technology, Science, Culture)
- **Minimalistic Design**: Clean and easy-to-read interface
- **One Article Per Source**: Displays one article from each news source per day
- **Responsive**: Works on desktop, tablet, and mobile devices
- **Optimized Performance**: Only stores current date's data (keeps JSON ~386KB vs potential 11+MB accumulation)

## Configuration

The UI fetches data from the GitHub Gist specified in `index.html`:
- GIST_ID: `17c58ca69bfa6f204a353a76f21b7774`
- GIST_FILENAME: `magazine-articles.json`

## Deployment

The UI is automatically deployed to GitHub Pages when changes are pushed to the `docs/` folder in the main branch.

Visit the live site at: https://pappater.github.io/articlay/
