# Unit Testing  for booksdatasource.py
# @author Charlie Broadbent
# @author Will Thompson

import unittest
import booksdatasource

class BooksDataSourceTest(unittest.TestCase)        
    
    def test_retrieving_book_beginning_edge_case(self):
        self.assertEqual(booksdatasource.book(0), "All Clear")
    
    def test_retrieving_book_middle_edge_case(self):
        self.assertEqual(booksdatasource.book(40), "Three Men in a Boat (to Say Nothing of the Dog)")
    
    def test_retrieving_book_end_edge_case(self):
        self.assertEqual(booksdatasource.book(46), "The Spy Who Came in From the Cold")
    
    def test_retrieving_book_by_author(self):
        self.assertEqual(booksdatasource.books(17), ["My Ántonia","O Pioneers!"]
    
    def test_retrieving_book_by_search_text(self, *, search_text=None):
        pass
    
    def test_retrieving_book_by_start_year(self, *, start_year=None):
        pass
        
    def test_retrieving_book_by_end_year(self, *, end_year=None):
        pass
        
    def test_retrieving_author(self, author_id):
        pass
        
    def test_retrieving_author_by_book_id(self, *, book_id=None):
        pass
        
    def test_retrieving_author_by_search_text(self, *, search_text=None):
        pass
    
    def test_retrieving_author_by_start_year(self, *, start_year=None):
        pass
        
    def test_retrieving_author_by_end_year(self, *, end_year=None):
        pass

    def test_retrieving_books_for_author(self, author_id):
        pass

    def test_retrieving_authors_for_book(self, book_id):
        pass
