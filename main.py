"""
Interactive Command Line Interface Execution Core.
Satisfies Functional Module 3: User Interaction & Workflow.
"""

import sys
from library_ops import LibraryManager
from recommender import get_recommendations_for_user
from validator import validate_menu_choice, sanitize_string

def seed_data(manager: LibraryManager):
    """Pre-populates sample data for testing."""
    manager.add_book("B101", "Python Programming", "Guido van Rossum", "Tech", ["python", "coding", "software"])
    manager.add_book("B102", "Data Structures in Python", "Goodrich", "Tech", ["python", "algorithms", "data"])
    manager.add_book("B103", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", ["classic", "novel", "drama"])
    manager.add_book("B104", "Clean Code", "Robert C. Martin", "Tech", ["coding", "software", "best_practices"])
    manager.add_book("B105", "To Kill a Mockingbird", "Harper Lee", "Fiction", ["classic", "drama", "history"])
    
    manager.register_user("U101", "Alice")
    manager.register_user("U102", "Bob")

def main():
    manager = LibraryManager()
    seed_data(manager)

    while True:
        print("\n" + "="*45)
        print(" DIGITAL LIBRARY & RECOMMENDATION SYSTEM ")
        print("="*45)
        print("1. View All Books")
        print("2. Search Book by Title/Author")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Get Personalized Book Recommendations")
        print("6. Add New Book")
        print("7. Exit")
        print("="*45)

        choice_input = input("Enter option (1-7): ")
        choice = validate_menu_choice(choice_input, 7)

        if choice == -1:
            print("[X] Invalid option! Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            print("\n--- Catalog ---")
            for b_id, book in manager.catalog.items():
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"[{b_id}] {book.title} by {book.author} | Genre: {book.genre} | Status: {status}")

        elif choice == 2:
            q = input("Enter search keyword: ")
            results = manager.search_books_by_title_or_author(q)
            if results:
                print(f"\nFound {len(results)} matching book(s):")
                for book in results:
                    print(f"- [{book.book_id}] {book.title} by {book.author}")
            else:
                print("[!] No matching books found.")

        elif choice == 3:
            u_id = input("Enter User ID (e.g., U101): ").strip()
            b_id = input("Enter Book ID (e.g., B101): ").strip()
            success, msg = manager.borrow_book(u_id, b_id)
            print(f"[{'✓' if success else 'X'}] {msg}")

        elif choice == 4:
            u_id = input("Enter User ID: ").strip()
            b_id = input("Enter Book ID: ").strip()
            success, msg = manager.return_book(u_id, b_id)
            print(f"[{'✓' if success else 'X'}] {msg}")

        elif choice == 5:
            u_id = input("Enter User ID to get recommendations: ").strip()
            if u_id not in manager.users:
                print("[X] User not found.")
                continue
            user = manager.users[u_id]
            recs = get_recommendations_for_user(user, manager.catalog)
            print(f"\n--- Recommended Books for {user.name} ---")
            if recs:
                for book in recs:
                    print(f"★ [{book.book_id}] {book.title} (Genre: {book.genre})")
            else:
                print("[!] No recommendations available. Borrow a few books first to build profile preferences!")

        elif choice == 6:
            b_id = input("Enter Book ID: ").strip()
            title = sanitize_string(input("Enter Book Title: "))
            author = sanitize_string(input("Enter Author: "))
            genre = sanitize_string(input("Enter Genre: "))
            tags = [t.strip().lower() for t in input("Enter Tags (comma separated): ").split(",")]
            if manager.add_book(b_id, title, author, genre, tags):
                print("[✓] Book successfully added to library catalog!")
            else:
                print("[X] Book ID already exists.")

        elif choice == 7:
            print("Thank you for using Digital Library System. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()
