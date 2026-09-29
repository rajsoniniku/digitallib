"""
Data Models and Storage representation using Python Dictionaries, Lists, and Sets.
Aligned with CSE1021 syllabus: Compound data structures.
"""

class Book:
    def __init__(self, book_id: str, title: str, author: str, genre: str, tags: list):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.tags = set(tags)  # Using Sets for fast comparison
        self.is_borrowed = False

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "tags": list(self.tags),
            "is_borrowed": self.is_borrowed
        }

class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  # List of book_ids
        self.reading_history_tags = set()  # Set of genre/tags user likes

    def borrow_book(self, book_id: str, book_tags: set):
        self.borrowed_books.append(book_id)
        # Update user's interest set using Set Union operation
        self.reading_history_tags = self.reading_history_tags.union(book_tags)

    def return_book(self, book_id: str):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
