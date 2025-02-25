import pytest
from classes.many_to_many import Article, Magazine, Author

class TestMagazine:
    """Magazine in many_to_many.py"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        
        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_immutable_string(self):
        """Magazine name is of type str and cannot be changed"""
        magazine = Magazine("Vogue", "Fashion")
        assert isinstance(magazine.name, str)
        with pytest.raises(AttributeError):
            magazine.name = "New Yorker"

    def test_name_len(self):
        """Magazine name is between 2 and 16 characters"""
        with pytest.raises(ValueError):
            Magazine("A", "Fashion")
        with pytest.raises(ValueError):
            Magazine("A" * 17, "Fashion")

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine = Magazine("Vogue", "Fashion")
        assert magazine.category == "Fashion"
    
    def test_category_is_non_empty_string(self):
        """Magazine category is a non-empty string"""
        with pytest.raises(ValueError):
            Magazine("Vogue", "")
        with pytest.raises(TypeError):
            Magazine("Vogue", 123)
    
    def test_has_many_articles(self):
        """Magazine has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")
        
        assert len(magazine.articles()) == 2
        assert article_1 in magazine.articles()
        assert article_2 in magazine.articles()
    
    def test_articles_are_instances_of_article(self):
        """Magazine articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert isinstance(magazine.articles()[0], Article)

    def test_has_many_contributors(self):
        """Magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")
        
        assert len(magazine.contributors()) == 2
        assert author_1 in magazine.contributors()
        assert author_2 in magazine.contributors()
    
    def test_contributors_are_unique(self):
        """Magazine contributors are unique"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "How to be single and happy")
        
        assert len(set(magazine.contributors())) == len(magazine.contributors())
        assert len(magazine.contributors()) == 1
    
    def test_article_titles(self):
        """Returns a list of titles of all articles in the magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        assert magazine.article_titles() == ["How to wear a tutu with style"]
    
    def test_contributing_authors(self):
        """Returns authors who have written more than 2 articles for the magazine"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "Article 1")
        Article(author_1, magazine, "Article 2")
        Article(author_1, magazine, "Article 3")
        Article(author_2, magazine, "Article 4")
        
        assert author_1 in magazine.contributing_authors()
        assert author_2 not in magazine.contributing_authors()
    
    def test_top_publisher(self):
        """Returns the magazine with the most articles"""
        Magazine.all = []
        author = Author("Carry Bradshaw")
        mag_1 = Magazine("Vogue", "Fashion")
        mag_2 = Magazine("AD", "Architecture")
        
        assert Magazine.top_publisher() is None
        
        Article(author, mag_1, "Article 1")
        Article(author, mag_1, "Article 2")
        Article(author, mag_1, "Article 3")
        Article(author, mag_2, "Article 4")
        
        assert Magazine.top_publisher() == mag_1
        assert isinstance(Magazine.top_publisher(), Magazine)
