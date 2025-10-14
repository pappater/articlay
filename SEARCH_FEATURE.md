# Articlay Search Feature Documentation

## Overview

The Articlay web UI now includes a powerful search feature that allows users to find articles by keywords or source names. The search functionality is integrated directly into the main web interface and provides real-time filtering of articles.

## Features

### 🔍 Search Types
- **All Fields**: Search across source names, article titles, descriptions, and categories
- **Source Only**: Search specifically in source names (e.g., "forbes", "cnn", "bbc")
- **Title Only**: Search only in article titles
- **Description Only**: Search only in article descriptions  
- **Category Only**: Search only in article categories

### 🚀 Key Capabilities
- **Real-time Search**: Results update as you type (with 300ms debounce)
- **Case-insensitive**: Search works regardless of capitalization
- **Partial Matching**: Find "tech" in "technology", "TechCrunch", etc.
- **Multi-source Results**: Shows matching articles from all relevant sources
- **Search Results Counter**: Displays number of matching articles and sources
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## How to Use

### Basic Search
1. Open the Articlay web interface
2. Use the search bar in the header (below the title)
3. Type your search query (e.g., "forbes", "technology", "covid")
4. Results will appear automatically as you type

### Advanced Search
1. Use the dropdown filter to choose search scope:
   - **All Fields** (default): Search everywhere
   - **Source Only**: Find specific news sources
   - **Title Only**: Search article headlines
   - **Description Only**: Search article content
   - **Category Only**: Filter by topic categories

2. Use the **Clear** button to reset search and return to all articles

### Search Examples

#### Finding Specific Sources
- Search: `forbes` → Shows all Forbes articles
- Search: `reddit` → Shows all Reddit posts
- Search: `hindu` → Shows The Hindu newspaper articles
- Search: `cnn` → Shows CNN news articles

#### Finding Topics/Keywords
- Search: `technology` → Shows tech-related articles from all sources
- Search: `covid` → Shows COVID-related news
- Search: `election` → Shows election coverage
- Search: `climate` → Shows climate change articles

#### Targeted Searches
- Source Only + `bbc` → Only BBC articles
- Title Only + `AI` → Articles with "AI" in the title
- Category Only + `business` → All business category articles

## Technical Implementation

### Search Architecture
- **Debounced Input**: 300ms delay prevents excessive filtering
- **In-memory Filtering**: Fast client-side search without server requests
- **State Management**: Preserves original data for quick search clearing
- **Tab Integration**: Search results maintain category organization

### Search Algorithm
1. **Query Processing**: Convert to lowercase for case-insensitive matching
2. **Field Filtering**: Apply search to selected fields based on filter type
3. **Result Compilation**: Collect matching articles across all sources
4. **Category Organization**: Group results by existing categories
5. **UI Update**: Refresh tabs and display search statistics

### Data Flow
```
User Input → Debounce → Filter Articles → Organize by Category → Update UI → Show Results Info
```

## Code Structure

### Key Functions
- `handleSearchInput()`: Main search handler with debouncing
- `performSearch(query, filterType)`: Execute search logic
- `filterArticles(articles, query, filterType)`: Core filtering algorithm
- `showSearchResultsInfo()`: Display search statistics
- `clearSearch()`: Reset to original article view

### CSS Classes
- `.search-bar`: Main search container
- `.search-input`: Search text input
- `.search-filters`: Filter controls container
- `.filter-select`: Dropdown filter selector
- `.clear-search-btn`: Clear search button
- `.search-results-info`: Search results information bar

## Browser Compatibility

The search feature works on all modern browsers:
- ✅ Chrome (60+)
- ✅ Firefox (55+)
- ✅ Safari (12+)
- ✅ Edge (79+)
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- **Client-side Processing**: No server requests needed for search
- **Debounced Input**: Prevents excessive processing while typing
- **Efficient Filtering**: O(n) complexity for article filtering
- **Memory Management**: Temporary storage of original data during search

## Responsive Design

### Desktop (>768px)
- Horizontal search bar layout
- Full-width search input with inline filters
- Compact results information

### Mobile (≤768px)
- Vertical search bar layout
- Full-width stacked components
- Touch-friendly button sizes
- Optimized typography

## Future Enhancements

Potential improvements for future versions:
- **Search History**: Remember recent searches
- **Advanced Filters**: Date range, source type filtering
- **Search Suggestions**: Auto-complete for sources and topics
- **Regex Search**: Pattern-based search for power users
- **Export Search Results**: Download filtered articles
- **Bookmarkable Searches**: URL parameters for sharing searches

## Troubleshooting

### Common Issues
1. **No Search Results**: Check spelling, try broader terms
2. **Search Not Working**: Ensure JavaScript is enabled
3. **Mobile Layout Issues**: Try refreshing the page
4. **Performance Slow**: Clear browser cache

### Debug Mode
For developers, you can check search functionality in browser console:
```javascript
// Check if search is active
console.log('Search Active:', isSearchActive);

// View original articles
console.log('Original Articles:', originalArticles);

// View current filtered articles
console.log('Current Articles:', allData[currentDate]);
```

## Contributing

To contribute to the search feature:
1. The main search logic is in the `<script>` section of `docs/index.html`
2. CSS styling is in the `<style>` section of the same file
3. Test all search scenarios before submitting changes
4. Ensure mobile responsiveness is maintained

---

**Last Updated**: October 2024  
**Version**: 1.0  
**Author**: Articlay Development Team