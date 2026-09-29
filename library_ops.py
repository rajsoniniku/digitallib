"""
Core Library Operations (CRUD operations & Array processing).
Applies CSE1021 concepts: List manipulation, Dictionaries, and Searching.
"""

from models import Book, User

class LibraryManager:
    def __init__(self):
        self.catalog = {}  # Dictionary: {book_id: Book object}
        self.users = {}    # Dictionary: {user_id: User object}

    def add_book(self, book_id: str, title: str, author: str, genre: str, tags: list) -> bool:
        """Adds a new book record to the catalog."""
        if book_id in self.catalog:
            return False
        new_book = Book(book_id, title, author, genre, tags)
        self.catalog[book_id] = new_book
        return True

    def register_user(self, user_id: str, name: str) -> bool:
        """Registers a user profile."""
        if user_id in self.users:
            return False
        self.users[user_id] = User(user_id, name)
        return True

    def search_books_by_title_or_author(self, query: str) -> list:
        """Linear search matching substring across book list."""
        query_lower = query.lower()
        results = []
        for book in self.catalog.values():
            if query_lower in book.title.lower() or query_lower in book.author.lower():
                results.append(book)
        return results

    def borrow_book(self, user_id: str, book_id: str) -> (bool, str):
        """Processes book issue logic."""
        if user_id not in self.users:
            return False, "User ID not found."
        if book_id not in self.catalog:
            return False, "Book ID not found."
        
        book = self.catalog[book_id]
        if book.is_borrowed:
            return False, "Book is currently borrowed by another user."

        book.is_borrowed = True
        user = self.users[user_id]
        user.borrow_book(book_id, book.tags)
        return True, f"Book '{book.title}' successfully issued!"

    def return_book(self, user_id: str, book_id: str) -> (bool, str):
        """Processes book return logic."""
        if user_id not in self.users or book_id not in self.catalog:
            return False, "Invalid User ID or Book ID."
        
        user = self.users[user_id]
        if book_id not in user.borrowed_books:
            return False, "This user hasn't borrowed this book."

        book = self.catalog[book_id]
        book.is_borrowed = False
        user.return_book(book_id)
        return True, f"Book '{book.title}' successfully returned!"
