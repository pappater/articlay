#!/usr/bin/env python3
"""Basic tests for Articlay"""

import unittest
from unittest.mock import Mock, patch
from articlay import MagzterScraper, GistArchiver, Articlay


class TestMagzterScraper(unittest.TestCase):
    """Test MagzterScraper functionality"""
    
    def setUp(self):
        self.scraper = MagzterScraper()
    
    def test_get_popular_magazines(self):
        """Test fetching popular magazines"""
        magazines = self.scraper.get_popular_magazines(10)
        self.assertEqual(len(magazines), 10)
        self.assertIn('name', magazines[0])
        self.assertIn('url', magazines[0])
        self.assertIn('latest_edition', magazines[0])
    
    def test_get_popular_magazines_limit(self):
        """Test magazine limit is respected"""
        for limit in [10, 20, 30]:
            magazines = self.scraper.get_popular_magazines(limit)
            self.assertEqual(len(magazines), limit)
    
    def test_get_articles_from_magazine(self):
        """Test article extraction from magazine"""
        magazine = {
            'name': 'Test Magazine',
            'url': 'https://www.magzter.com/test',
            'latest_edition': 'Edition 2024-01'
        }
        articles = self.scraper.get_articles_from_magazine(magazine)
        self.assertGreater(len(articles), 0)
        self.assertIn('title', articles[0])
        self.assertIn('link', articles[0])
        self.assertIn('magazine', articles[0])


class TestGistArchiver(unittest.TestCase):
    """Test GistArchiver functionality"""
    
    def test_no_token_warning(self):
        """Test warning when no token provided"""
        archiver = GistArchiver()
        self.assertIsNone(archiver.token)
    
    def test_token_from_parameter(self):
        """Test token can be provided as parameter"""
        archiver = GistArchiver("test_token")
        self.assertEqual(archiver.token, "test_token")
    
    @patch.dict('os.environ', {'GITHUB_TOKEN': 'env_token'})
    def test_token_from_environment(self):
        """Test token can be read from environment"""
        archiver = GistArchiver()
        self.assertEqual(archiver.token, "env_token")


class TestArticlay(unittest.TestCase):
    """Test Articlay main functionality"""
    
    def setUp(self):
        self.app = Articlay()
    
    def test_select_random_articles(self):
        """Test random article selection"""
        magazines = [
            {'name': f'Magazine {i}', 'url': f'https://example.com/mag{i}', 
             'latest_edition': 'Edition 2024'}
            for i in range(1, 11)
        ]
        
        articles = self.app.select_random_articles(magazines, count=5)
        self.assertEqual(len(articles), 5)
        
        # Check all articles are from different magazines
        magazine_names = [a['magazine'] for a in articles]
        self.assertEqual(len(magazine_names), len(set(magazine_names)))
    
    def test_select_more_articles_than_magazines(self):
        """Test selection when requesting more articles than magazines"""
        magazines = [
            {'name': f'Magazine {i}', 'url': f'https://example.com/mag{i}',
             'latest_edition': 'Edition 2024'}
            for i in range(1, 4)  # Only 3 magazines
        ]
        
        articles = self.app.select_random_articles(magazines, count=5)
        # Should only get 3 articles (one per magazine)
        self.assertEqual(len(articles), 3)
    
    def test_run_no_archive(self):
        """Test main run without archiving"""
        articles = self.app.run(magazine_count=10, article_count=5, archive=False)
        self.assertGreater(len(articles), 0)
        self.assertLessEqual(len(articles), 5)


if __name__ == '__main__':
    unittest.main()
