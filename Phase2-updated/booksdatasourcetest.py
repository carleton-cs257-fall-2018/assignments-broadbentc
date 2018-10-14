# Refined Unit Testing  for booksdatasource.py
# @author Charlie Broadbent
# @author Will Thompson

import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):

    def setUp(self):
        self.booksdatasource = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")
        self.anotherbooksdatasource = booksdatasource.BooksDataSource("books_test.csv", "authors_test.csv", "books_authors.csv")

    def tearDown(self):
        pass

    '''This Section contains unit tests for books(self, book_id) method'''


    def test_retrieving_book_beginning_id(self):
        self.assertEqual(self.booksdatasource.book(0), {'id': 0, 'title': 'All Clear', 'publication_year': 2010})

    def test_retrieving_book_middle_id(self):
        self.assertEqual(self.booksdatasource.book(40),
                         {'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)',
                          'publication_year': 1889})

    def test_retrieving_book_end_id(self):
        self.assertEqual(self.booksdatasource.book(46),
                         {'id': 46, 'title': 'The Spy Who Came in From the Cold', 'publication_year': 1963})



    '''This Section contains unit tests for 
       books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title') method'''




    def test_retrieving_book_by_author(self):
        self.assertEqual(self.booksdatasource.books(author_id=17),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918},
                          {'id': 34, 'title': 'O Pioneers!', 'publication_year': 1913}])

    def test_retrieving_book_by_author_and_startyear_with_startyear_including_all_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1900),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918},
                          {'id': 34, 'title': 'O Pioneers!', 'publication_year': 1913}])

    def test_retrieving_book_by_author_and_startyear_with_a_year_splitting_the_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1915),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918}])

    def test_retrieving_book_by_author_and_startyear_checking_a_year_equal_to_the_publication_year(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1918),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918}])

    def test_retrieving_book_by_author_and_startyear_where_the_inputted_year_returns_no_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1920), [])

    def test_retrieving_book_by_author_and_endyear_with_endyear_including_all_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1900),
                         [{'id': 13, 'title': 'Moby Dick', 'publication_year': 1851},
                          {'id': 16, 'title': 'Omoo', 'publication_year': 1847}])

    def test_retrieving_book_by_author_and_endyear_with_endyear_splitting_the_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1850),
                         [{'id': 16, 'title': 'Omoo', 'publication_year': 1847}])

    def test_retrieving_book_by_author_and_endyear_checking_a_year_equal_to_the_publication_year(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1847),
                         [{'id': 16, 'title': 'Omoo', 'publication_year': 1847}])

    def test_retrieving_book_by_author_and_endyear_where_the_inputted_year_returns_no_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1800), [])

    def test_retrieving_book_by_author_and_endyear_where_all_books_by_author_have_same_publication_year(self):
        self.assertEqual(self.booksdatasource.books(author_id=20, end_year=2020),
                         [{'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015},
                          {'id': 38, 'title': 'The Obelisk Gate', 'publication_year': 2015},
                          {'id': 39, 'title': 'The Stone Sky', 'publication_year': 2015}])

    def test_retrieving_book_by_author_and_endyear_checking_a_year_equal_to_all_books_publication_years(self):
        self.assertEqual(self.booksdatasource.books(author_id=20, end_year=2015),
                         [{'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015},
                          {'id': 38, 'title': 'The Obelisk Gate', 'publication_year': 2015},
                          {'id': 39, 'title': 'The Stone Sky', 'publication_year': 2015}])

    def test_retrieving_book_by_author_and_endyear_where_inputted_year_returns_no_books(self):
        self.assertEqual(self.booksdatasource.books(author_id=20, end_year=2014), [])

    def test_retrieving_book_by_text_checking_for_case_sensitivity_with_capitalized_and_uncapitalized_letters(self):
        self.assertEqual(self.booksdatasource.books(search_text='Mi'),
                         [{'id': 11, 'title': "Midnight's Children", 'publication_year': 1981},
                          {'id': 12, 'title': "Mirror", 'publication_year': 1994},
                          {'id': 41, 'title': "Middlemarch", 'publication_year': 1871}])

    def test_retrieving_book_by_text_checking_for_case_sensitivity_with_uncapitalized_letters(self):
        self.assertEqual(self.booksdatasource.books(search_text='mi'),
                         [{'id': 11, 'title': "Midnight's Children", 'publication_year': 1981},
                          {'id': 12, 'title': "Mirror", 'publication_year': 1994},
                          {'id': 41, 'title': "Middlemarch", 'publication_year': 1871}])

    def test_retrieving_book_by_text_checking_for_case_sensitivity_with_capitalized_letters(self):
        self.assertEqual(self.booksdatasource.books(search_text='MI'),
                         [{'id': 11, 'title': "Midnight's Children", 'publication_year': 1981},
                          {'id': 12, 'title': "Mirror", 'publication_year': 1994},
                          {'id': 41, 'title': "Middlemarch", 'publication_year': 1871}])

    def test_retrieving_book_by_multiple_input_search_tex_as_title(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="All Clear"),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])
    
    def test_retrieving_book_by_multiple_input_with_entire_title_with_inclusive_start_end_years(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="All Clear", start_year=2010, end_year=2011),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input_with_entire_title_with_inclusive_start_only(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="All Clear", start_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])
        
    def test_retrieving_book_by_multiple_input_with_entire_title_with_inclusive_endyear_only(self): 
        self.assertEqual(self.booksdatasource.books(author_id=0, end_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input_checking_case_sensitivity_of_search_text_with_partial_title(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="ar"),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input_checking_case_sensitivity_of_search_text_with_partial_title(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="AR"),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input_with_publication_year_equal_to_start_end_years(self): 
        self.assertEqual(self.booksdatasource.books(author_id=0, start_year=2010, end_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input_with_equal_startyear_inclusive_end_year(self):  
        self.assertEqual(self.booksdatasource.books(author_id=0, start_year=2010, end_year=2011),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input_with_inclusive_start_year_and_equal_endyear(self): 
        self.assertEqual(self.booksdatasource.books(author_id=0, start_year=2009, end_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_sorting_by_title(self):
        self.assertEqual(self.anotherbooksdatasource.books(sort_by='title'),
                         [{'id': 9, 'title': "Love in the Time of Cholera", 'publication_year': 1985},
                          {'id': 10, 'title': "Main Street", 'publication_year': 1920},
                          {'id': 19, 'title': "Right Ho", 'publication_year': 2010},
                          {'id': 46, 'title': "The Spy Who Came in From the Cold", 'publication_year': 1963}])

    def test_sorting_by_year(self):
        self.assertEqual(self.anotherbooksdatasource.books(sort_by='title'),
                         [{'id': 10, 'title': "Main Street", 'publication_year': 1920},
                          {'id': 46, 'title': "The Spy Who Came in From the Cold", 'publication_year': 1963},
                          {'id': 9, 'title': "Love in the Time of Cholera", 'publication_year': 1985},
                          {'id': 19, 'title': "Right Ho", 'publication_year': 2010}])




    '''This section contains unit tests for the author(self, author_id) method'''




    def test_retrieving_book_beginning_id(self):
        self.assertEqual(self.booksdatasource.book(0),
                         {'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945,'death_year': None})

    def test_retrieving_book_middle_id(self):
        self.assertEqual(self.booksdatasource.book(2),
                         {'id': 2, 'last_name': 'Morrison', 'first_name': 'Toni', 'birth_year': 1931,'death_year': None})

    def test_retrieving_book_end_id(self):
        self.assertEqual(self.booksdatasource.book(24),
                         {'id': 24, 'last_name': 'Carré', 'first_name': 'John', 'birth_year': 1931, 'death_year': None})




    ''' This section contains unit tests for the
        authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year') method
    '''
    
    def test_retrieving_author_by_multiple_input(self):
        self.assertEqual(self.booksdatasource.authors(book_id = 24,start_year = 1930), 
        [{'id':11, 'last_name': 'Rushdie', 'first_name': 'Salman','birth_year': 1947, 'death_year': 'NULL'}])
        
    def test_retrieving_author_by_book_id_with_multiple_authors(self):
        self.assertEqual(self.booksdatasource.authors(book_id = 6, sort_by = 'last_name'), 
        [{'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil','birth_year': 1960, 'death_year': 'NULL'},
         {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': 2015}])

    def test_retrieving_author_by_search_text_parameter(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'N.K.'), 
        [{'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.','birth_year': 1972, 'death_year': 'NULL'}])

    def test_retrieving_author_by_search_text_with_same_lastname_testing_for_case_sensitivity_one_capitalized_letter(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'Brontë', sort_by = 'last_name'), 
        [{'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann','birth_year': 1820, 'death_year': 1849},
         {'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily','birth_year': 1818, 'death_year': 1848}])

    def test_retrieving_author_by_search_text_with_same_lastname_testing_for_case_sensitivity_two_capitalized_letters(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'BRontë', sort_by = 'last_name'), 
        [{'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann','birth_year': 1820, 'death_year': 1849},
         {'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily','birth_year': 1818, 'death_year': 1848}])

    def test_retrieving_author_by_search_text_with_same_lastname_testing_for_case_sensitivity_no_capitalized_letters(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'brontë', sort_by = 'last_name'), 
        [{'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann','birth_year': 1820, 'death_year': 1849},
         {'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily','birth_year': 1818, 'death_year': 1848}])
         
    def test_retrieving_author_by_search_text_with_same_lastname_testing_for_case_sensitivity_sorting_by_birthyear(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'brontë', sort_by = 'birth_year'), 
        [{'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily','birth_year': 1818, 'death_year': 1848},
         {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann','birth_year': 1820, 'death_year': 1849}])
    
    def test_retrieving_author_by_search_text_with_same_lastname_testing_for_case_sensitivity_and_testing_the_default_sorting_feature(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'brontë'), 
        [{'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily','birth_year': 1818, 'death_year': 1848},
         {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann','birth_year': 1820, 'death_year': 1849}])

    def test_retrieving_author_by_search_text_with_single_letter(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 'k', sort_by = 'last_name'), 
        [{'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870},
         {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.','birth_year': 1972, 'death_year': 'NULL'}, 
         {'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.','birth_year': 1859, 'death_year': 1927},
         {'id': 16, 'last_name': 'Murakami', 'first_name': 'Haruki','birth_year': 1949, 'death_year': 'NULL'}])

    def test_retrieving_author_by_start_year(self):
        self.assertEqual(self.anotherbooksdatasource.authors(start_year= 1800, sort_by = 'last_name'), 
        [{'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855},
         {'id':24, 'last_name': 'Carré', 'first_name': 'John Le','birth_year': 1931, 'death_year': 'NULL'},
         {'id':13, 'last_name': 'Melville', 'first_name': 'Herman','birth_year': 1819, 'death_year': 1891},
         {'id':0, 'last_name': 'Willis', 'first_name': 'Connie','birth_year': 1945, 'death_year': 'NULL'}])

    def test_retrieving_author_by_start_year_to_test_how_NULL_values_behave(self):
        self.assertEqual(self.anotherbooksdatasource.authors(start_year = 2000, sort_by = 'last_name'), 
        [{'id':24, 'last_name': 'Carré', 'first_name': 'John Le','birth_year': 1931, 'death_year': 'NULL'},
         {'id':0, 'last_name': 'Willis', 'first_name': 'Connie','birth_year': 1945, 'death_year': 'NULL'}])
         
        
    def test_retrieving_author_by_end_year_testing_for_when_end_year_equals_birth_year(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1775), 
        [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])
         
    def test_retrieving_author_by_end_year_testing_for_when_end_year_is_one_year_more_than_birth_year(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1776), 
        [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

    def test_sorting_various_authors_by_end_year(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1820, sort_by = 'last_name'), 
        [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817},
         {'id':14, 'last_name': 'Brontë', 'first_name': 'Ann','birth_year': 1820, 'death_year': 1849}, 
         {'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855},
         {'id':15, 'last_name': 'Brontë', 'first_name': 'Emily','birth_year': 1818, 'death_year': 1848}, 
         {'id':23, 'last_name': 'Dickens', 'first_name': 'Charles','birth_year': 1812, 'death_year': 1870},
         {'id':22, 'last_name': 'Eliot', 'first_name': 'George','birth_year': 1819, 'death_year': 1880},
         {'id':13, 'last_name': 'Melville', 'first_name': 'Herman','birth_year': 1819, 'death_year': 1891}]) 
         

    def test_retrieving_author_by_end_year_tha_should_return_no_authors(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1700), [])

    def test_sorting_authors_by_lastname(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1930, end_year = 1950, sort_by='last_name'), 
        [{'id':12, 'last_name': 'Bujold', 'first_name': 'Lois McMaster','birth_year': 1949, 'death_year': 'NULL'},
        {'id':24, 'last_name': 'Carré', 'first_name': 'John Le','birth_year': 1931, 'death_year': 'NULL'},
        {'id':17, 'last_name': 'Cather', 'first_name': 'Willa','birth_year': 1873, 'death_year': 1947},
        {'id':1, 'last_name': 'Christie', 'first_name': 'Agatha','birth_year': 1890, 'death_year': 1976},
        {'id':19, 'last_name': 'DuMaurier', 'first_name': 'Daphne','birth_year': 1907, 'death_year': 1989},
        {'id':3, 'last_name': 'Lewis', 'first_name': 'Sinclair','birth_year': 1885, 'death_year': 'NULL'},
        {'id':10, 'last_name': 'Lewis', 'first_name': 'Sinclair','birth_year': 1885, 'death_year': 1951},
        {'id':2, 'last_name': 'Morrison', 'first_name': 'Toni','birth_year': 1931, 'death_year': 'NULL'},
        {'id':16, 'last_name': 'Murakami', 'first_name': 'Haruki','birth_year': 1949, 'death_year': 'NULL'}, 
        {'id':9, 'last_name': 'Márquez', 'first_name': 'Gabriel García','birth_year': 1927, 'death_year': 2014},
        {'id':6, 'last_name': 'Pratchett', 'first_name': 'Terry','birth_year': 1948, 'death_year': 2015},
        {'id':11, 'last_name': 'Rushdie', 'first_name': 'Salman','birth_year': 1947, 'death_year': 'NULL'},
        {'id':0, 'last_name': 'Willis', 'first_name': 'Connie','birth_year': 1945, 'death_year': 'NULL'},
        {'id':8, 'last_name': 'Wodehouse', 'first_name': 'Pelham Grenville','birth_year': 1881, 'death_year': 1975}])
        

    def test_retrieving_author_where_the_parameters_conflict_and_no_authors_are_returned(self):
        self.assertEqual(self.booksdatasource.authors(book_id = 5, start_year = 2000), [])

    def test_retrieving_author_by_start_year_and_end_year_testing_for_end_year_inclusion(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1774, end_year =1775), 
        [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

    def test_retrieving_author_multiple_input_testing_for_startyear_and_endyear_inclusion(self):
        self.assertEqual(self.booksdatasource.authors(start_year =  1775, end_year = 1775), 
        [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

    def test_retrieving_author_multiple_input_testing_for_start_year_inclusion(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1775, end_year =1776), 
        [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane','birth_year': 1775, 'death_year': 1817}])

    def test_sort_author_by_birth_year(self):
        self.assertEqual(self.anotherbooksdatasource.authors(sort_by = 'birth_year'), 
        [{'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id':13, 'last_name': 'Melville', 'first_name': 'Herman','birth_year': 1819, 'death_year': 1891}, 
         {'id':24, 'last_name': 'Carré', 'first_name': 'John Le','birth_year': 1931, 'death_year': 'NULL'}, 
         {'id':0, 'last_name': 'Willis', 'first_name': 'Connie','birth_year': 1945, 'death_year': 'NULL'}])
         
         
    def test_sort_author_by_last_name(self):
        self.assertEqual(self.anotherbooksdatasource.authors(sort_by = 'last_name'), 
        [{'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855},
         {'id':24, 'last_name': 'Carré', 'first_name': 'John Le','birth_year': 1931, 'death_year': 'NULL'}, 
         {'id':13, 'last_name': 'Melville', 'first_name': 'Herman','birth_year': 1819, 'death_year': 1891}, 
         {'id':0, 'last_name': 'Willis', 'first_name': 'Connie','birth_year': 1945, 'death_year': 'NULL'}])
         
    def test_sort_author_testing_for_the_default_sorting_feature_when_no_sort_by_parameter_is_specified(self):
        self.assertEqual(self.anotherbooksdatasource.authors(start_year = 1), 
        [{'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte','birth_year': 1816, 'death_year': 1855}, 
         {'id':13, 'last_name': 'Melville', 'first_name': 'Herman','birth_year': 1819, 'death_year': 1891}, 
         {'id':24, 'last_name': 'Carré', 'first_name': 'John Le','birth_year': 1931, 'death_year': 'NULL'}, 
         {'id':0, 'last_name': 'Willis', 'first_name': 'Connie','birth_year': 1945, 'death_year': 'NULL'}])    

if __name__ == '__main__':
    unittest.main()
    
    

    

