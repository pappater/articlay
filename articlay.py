#!/usr/bin/env python3
"""
Articlay - Magzter Article Aggregator
Gathers popular magazine articles and archives them to GitHub Gist
"""

import os
import sys
import json
import random
import argparse
from datetime import datetime
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup


class MagzterScraper:
    """Scraper for Magzter magazines and articles"""
    
    BASE_URL = "https://www.magzter.com"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_popular_magazines(self, limit: int = 10) -> List[Dict]:
        """
        Fetch popular magazines from Magzter
        
        Args:
            limit: Number of top magazines to fetch (10, 20, or 30)
        
        Returns:
            List of magazine dictionaries with name, url, and latest edition
        """
        magazines = []
        
        # For demonstration, since we can't actually access Magzter without proper auth
        # This would be the actual implementation structure
        try:
            # Placeholder: In real implementation, scrape from Magzter's popular section
            # url = f"{self.BASE_URL}/popular"
            # response = self.session.get(url)
            # soup = BeautifulSoup(response.content, 'html.parser')
            
            # For now, return sample data structure
            sample_magazines = [
                {
                    'name': f'Magazine {i}',
                    'url': f'{self.BASE_URL}/magazine-{i}',
                    'latest_edition': f'Edition {datetime.now().strftime("%Y-%m")}'
                }
                for i in range(1, limit + 1)
            ]
            magazines = sample_magazines[:limit]
            
        except Exception as e:
            print(f"Error fetching magazines: {e}")
        
        return magazines
    
    def get_articles_from_magazine(self, magazine: Dict) -> List[Dict]:
        """
        Extract articles from a magazine's latest edition
        
        Args:
            magazine: Magazine dictionary with url
        
        Returns:
            List of article dictionaries with title and link
        """
        articles = []
        
        try:
            # Placeholder: In real implementation, scrape articles from magazine page
            # response = self.session.get(magazine['url'])
            # soup = BeautifulSoup(response.content, 'html.parser')
            
            # For now, return sample articles
            for i in range(1, 6):
                articles.append({
                    'title': f"{magazine['name']} - Article {i}",
                    'link': f"{magazine['url']}/article-{i}",
                    'magazine': magazine['name']
                })
                
        except Exception as e:
            print(f"Error fetching articles from {magazine['name']}: {e}")
        
        return articles


class GistArchiver:
    """Handler for archiving articles to GitHub Gist"""
    
    GIST_API_URL = "https://api.github.com/gists"
    
    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv('GITHUB_TOKEN')
        if not self.token:
            print("Warning: No GitHub token provided. Gist archiving disabled.")
    
    def archive_articles(self, articles: List[Dict]) -> Optional[str]:
        """
        Archive articles to a GitHub Gist
        
        Args:
            articles: List of article dictionaries
        
        Returns:
            URL of the created gist, or None if failed
        """
        if not self.token:
            print("Cannot archive: No GitHub token available")
            return None
        
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"articlay-{date_str}.md"
        
        # Format articles as markdown
        content = f"# Articlay - Popular Magazine Articles\n"
        content += f"Date: {date_str}\n\n"
        
        for i, article in enumerate(articles, 1):
            content += f"## {i}. {article['title']}\n"
            content += f"**Magazine:** {article['magazine']}\n"
            content += f"**Link:** {article['link']}\n\n"
        
        gist_data = {
            "description": f"Articlay articles for {date_str}",
            "public": True,
            "files": {
                filename: {
                    "content": content
                }
            }
        }
        
        try:
            headers = {
                'Authorization': f'token {self.token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            response = requests.post(self.GIST_API_URL, 
                                   headers=headers, 
                                   json=gist_data)
            
            if response.status_code == 201:
                gist_url = response.json()['html_url']
                print(f"\n✓ Archived to Gist: {gist_url}")
                return gist_url
            else:
                print(f"Failed to create gist: {response.status_code}")
                print(response.text)
                return None
                
        except Exception as e:
            print(f"Error creating gist: {e}")
            return None


class Articlay:
    """Main application class"""
    
    def __init__(self, github_token: Optional[str] = None):
        self.scraper = MagzterScraper()
        self.archiver = GistArchiver(github_token)
    
    def select_random_articles(self, magazines: List[Dict], 
                              count: int = 5) -> List[Dict]:
        """
        Select random articles from different magazines
        
        Args:
            magazines: List of magazine dictionaries
            count: Number of articles to select
        
        Returns:
            List of selected article dictionaries
        """
        selected_articles = []
        used_magazines = set()
        
        # Shuffle magazines to randomize selection
        shuffled_magazines = magazines.copy()
        random.shuffle(shuffled_magazines)
        
        for magazine in shuffled_magazines:
            if len(selected_articles) >= count:
                break
            
            if magazine['name'] not in used_magazines:
                articles = self.scraper.get_articles_from_magazine(magazine)
                if articles:
                    # Pick a random article from this magazine
                    article = random.choice(articles)
                    selected_articles.append(article)
                    used_magazines.add(magazine['name'])
        
        return selected_articles
    
    def run(self, magazine_count: int = 10, article_count: int = 5, 
           archive: bool = True) -> List[Dict]:
        """
        Main execution flow
        
        Args:
            magazine_count: Number of top magazines to consider (10, 20, or 30)
            article_count: Number of articles to select
            archive: Whether to archive to Gist
        
        Returns:
            List of selected articles
        """
        print(f"\n📰 Articlay - Magzter Article Aggregator")
        print(f"{'=' * 50}\n")
        
        print(f"Fetching top {magazine_count} popular magazines...")
        magazines = self.scraper.get_popular_magazines(magazine_count)
        
        if not magazines:
            print("No magazines found!")
            return []
        
        print(f"Found {len(magazines)} magazines")
        print(f"\nSelecting {article_count} random articles from different magazines...")
        
        articles = self.select_random_articles(magazines, article_count)
        
        if not articles:
            print("No articles found!")
            return []
        
        # Display articles
        print(f"\n📚 Selected Articles:")
        print(f"{'-' * 50}\n")
        
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
            print(f"   Magazine: {article['magazine']}")
            print(f"   Link: {article['link']}\n")
        
        # Archive to Gist if requested
        if archive:
            self.archiver.archive_articles(articles)
        
        return articles


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Articlay - Aggregate popular magazine articles from Magzter'
    )
    
    parser.add_argument(
        '--magazines', '-m',
        type=int,
        choices=[10, 20, 30],
        default=10,
        help='Number of top magazines to consider (default: 10)'
    )
    
    parser.add_argument(
        '--articles', '-a',
        type=int,
        default=5,
        help='Number of articles to select (default: 5)'
    )
    
    parser.add_argument(
        '--no-archive',
        action='store_true',
        help='Skip archiving to GitHub Gist'
    )
    
    parser.add_argument(
        '--token', '-t',
        type=str,
        help='GitHub personal access token (or set GITHUB_TOKEN env var)'
    )
    
    args = parser.parse_args()
    
    # Get GitHub token from args or environment
    github_token = args.token or os.getenv('GITHUB_TOKEN')
    
    # Create and run application
    app = Articlay(github_token)
    articles = app.run(
        magazine_count=args.magazines,
        article_count=args.articles,
        archive=not args.no_archive
    )
    
    # Save to local file as backup
    date_str = datetime.now().strftime("%Y-%m-%d")
    output_file = f"articlay-{date_str}.json"
    
    with open(output_file, 'w') as f:
        json.dump(articles, f, indent=2)
    
    print(f"\n✓ Articles saved to: {output_file}")
    
    return 0 if articles else 1


if __name__ == '__main__':
    sys.exit(main())
