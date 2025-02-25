import pytest

from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestAuthor:
    """Author in many_to_many.py"""

    def test_has_name(self):
        """Author is initialized with a name"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        
        assert author_1.name == "Carry Bradshaw"
        assert author_2.name == "Nathaniel Hawthorne"

    def test_name_is_immutable_string(self):
        """author name is of type str and cannot change"""
        author = Author("Carry Bradshaw")
        
        assert isinstance(author.name, str)
        
        with pytest.raises(AttributeError):
            author.name = "New Name"
        
        with pytest.raises(ValueError):
            Author("")

    def test_has_many_articles(self):
        """author has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")
        
        assert len(author.articles()) == 2
        assert isinstance(author.articles(), list)
        assert article_1 in author.articles()
        assert article_2 in author.articles()

    def test_has_many_magazines(self):
        """author has many magazines"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_2, "2023 Eccentric Design Trends")
        
        assert isinstance(author.magazines(), list)
        assert magazine_1 in author.magazines()
        assert magazine_2 in author.magazines()

    def test_magazines_are_unique(self):
        """author magazines are unique"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Fashion Trends 2024")
        
        assert len(set(author.magazines())) == len(author.magazines())

    def test_add_article(self):
        """creates and returns a new article given a magazine and title"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article = author.add_article(magazine, "How to wear a tutu with style")
        
        assert isinstance(article, Article)
        assert article in author.articles()
        assert article in magazine.articles()

    def test_topic_areas(self):
        """returns a list of unique topic areas for all articles by author"""
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        author.add_article(magazine_1, "How to wear a tutu with style")
        author.add_article(magazine_2, "Interior Design Trends")
        
        assert isinstance(author.topic_areas(), list)
        assert set(author.topic_areas()) == {"Fashion", "Architecture"}
        
    def test_topic_areas_are_unique(self):
        """topic areas are unique"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        author.add_article(magazine, "How to wear a tutu with style")
        author.add_article(magazine, "Fashion in NYC")
        
        assert len(set(author.topic_areas())) == len(author.topic_areas())
        assert author.topic_areas() == ["Fashion"]
        
    def test_topic_areas_empty_case(self):
        """returns an empty list if author has no articles"""
        author = Author("New Writer")
        
        assert author.topic_areas() == []
