"""
Recommendation Engine using Set Operations (Jaccard Similarity).
Applies CSE1021 concepts: Sets (Intersection & Union), Flow Control, and Sorting.
"""

def calculate_jaccard_similarity(set_a: set, set_b: set) -> float:
    """Computes similarity coefficient between two sets: |A ∩ B| / |A ∪ B|."""
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    if not union:
        return 0.0
    return len(intersection) / len(union)

def get_recommendations_for_user(user, catalog: dict, top_n: int = 3) -> list:
    """
    Recommends unborrowed books based on tag overlap with user's reading history.
    """
    if not user.reading_history_tags:
        return []

    scores = []
    for book_id, book in catalog.items():
        # Skip if already borrowed or unavailable
        if book_id in user.borrowed_books or book.is_borrowed:
            continue

        similarity = calculate_jaccard_similarity(user.reading_history_tags, book.tags)
        if similarity > 0:
            scores.append((book, similarity))

    # Sort books by similarity score in descending order
    scores.sort(key=lambda x: x[1], reverse=True)
    return [book for book, score in scores[:top_n]]
