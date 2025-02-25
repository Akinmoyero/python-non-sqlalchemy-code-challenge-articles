class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = self._validate_title(title)  # Store as a private attribute
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # Read-only property

    @staticmethod
    def _validate_title(title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            return title
        raise ValueError("Title must be between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise ValueError("Author must be an instance of Author class.")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise ValueError("Magazine must be an instance of Magazine class.")

class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")

    @property
    def name(self):
        return self._name  # No setter (Immutable)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return []
        return list(set(article.magazine.category for article in self.articles()))


class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name  # Immutable name
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        
        self.category = category  # Uses setter for validation
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name  # No setter (Immutable)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and new_category.strip():
            self._category = new_category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all or all(len(mag.articles()) == 0 for mag in cls.all):
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)
class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name  # Immutable name
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        
        self.category = category  # Uses setter for validation
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name  # No setter (Immutable)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and new_category.strip():
            self._category = new_category
        else:
            raise ValueError("Category must be a non-empty string.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all or all(len(mag.articles()) == 0 for mag in cls.all):
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)
class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name  # Immutable name
        else:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        
        self.category = category  # Uses setter for validation
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name  # No setter (Immutable)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):  
            raise TypeError("Category must be a string.")  # TypeError if not a string
        if not new_category.strip():
            raise ValueError("Category must be a non-empty string.")  # ValueError if empty
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2]

    @classmethod
    def top_publisher(cls):
        if not cls.all or all(len(mag.articles()) == 0 for mag in cls.all):
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()), default=None)
