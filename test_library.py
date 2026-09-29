"""
Unit Tests for Library Operations and Recommender.
Satisfies Section 3 Technical Expectations: Testing.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from library_ops import LibraryManager
from recommender import get_recommendations_for_user, calculate_jaccard_similarity

def test_add_and_borrow_book():
    mgr = LibraryManager()
    mgr.add_book("B1", "Test Book", "Author A", "Tech", ["python"])
    mgr.register_user("U1", "User A")
    
    success, _ = mgr.borrow_book("U1", "B1")
    assert success == True
    assert mgr.catalog["B1"].is_borrowed == True

def test_jaccard_similarity():
    set1 = {"python", "coding"}
    set2 = {"python", "data"}
    # Intersection = 1, Union = 3, Similarity = 1/3 = 0.333...
    sim = calculate_jaccard_similarity(set1, set2)
    assert round(sim, 2) == 0.33

if __name__ == "__main__":
    test_add_and_borrow_book()
    test_jaccard_similarity()
    print("All unit tests passed successfully!")
