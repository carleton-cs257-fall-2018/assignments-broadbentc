# Unit Testing  for booksdatasource.py
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


    def test_retrieving_book_beginning_edge_case(self):
        self.assertEqual(self.booksdatasource.book(0), {'id': 0, 'title': 'All Clear', 'publication_year': 2010})

    def test_retrieving_book_middle_edge_case(self):
        self.assertEqual(self.booksdatasource.book(40),
                         {'id': 40, 'title': 'Three Men in a Boat (to Say Nothing of the Dog)',
                          'publication_year': 1889})

    def test_retrieving_book_end_edge_case(self):
        self.assertEqual(self.booksdatasource.book(46),
                         {'id': 46, 'title': 'The Spy Who Came in From the Cold', 'publication_year': 1963})



    '''This Section contains unit tests for 
       books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title') 
       method
    '''




    def test_retrieving_book_by_author(self):
        self.assertEqual(self.booksdatasource.books(author_id=17),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918},
                          {'id': 34, 'title': 'O Pioneers!', 'publication_year': 1913}])

    def test_retrieving_book_by_author_and_startyear1(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1900),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918},
                          {'id': 34, 'title': 'O Pioneers!', 'publication_year': 1913}])

    def test_retrieving_book_by_author_and_startyear2(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1915),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918}])

    def test_retrieving_book_by_author_and_startyear3(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1918),
                         [{'id': 33, 'title': 'My Ántonia', 'publication_year': 1918}])

    def test_retrieving_book_by_author_and_startyear4(self):
        self.assertEqual(self.booksdatasource.books(author_id=17, start_year=1920), [])

    def test_retrieving_book_by_author_and_endyear1(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1900),
                         [{'id': 13, 'title': 'Moby Dick', 'publication_year': 1851},
                          {'id': 16, 'title': 'Omoo', 'publication_year': 1847}])

    def test_retrieving_book_by_author_and_endyear2(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1850),
                         [{'id': 16, 'title': 'Omoo', 'publication_year': 1847}])

    def test_retrieving_book_by_author_and_endyear3(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1847),
                         [{'id': 16, 'title': 'Omoo', 'publication_year': 1847}])

    def test_retrieving_book_by_author_and_endyear4(self):
        self.assertEqual(self.booksdatasource.books(author_id=13, end_year=1800), [])

    def test_retrieving_book_by_author_and_endyear5(self):
        self.assertEqual(self.booksdatasource.books(author_id=20, end_year=2020),
                         [{'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015},
                          {'id': 38, 'title': 'The Obelisk Gate', 'publication_year': 2015},
                          {'id': 39, 'title': 'The Stone Sky', 'publication_year': 2015}])

    def test_retrieving_book_by_author_and_endyear6(self):
        self.assertEqual(self.booksdatasource.books(author_id=20, end_year=2015),
                         [{'id': 37, 'title': 'The Fifth Season', 'publication_year': 2015},
                          {'id': 38, 'title': 'The Obelisk Gate', 'publication_year': 2015},
                          {'id': 39, 'title': 'The Stone Sky', 'publication_year': 2015}])

    def test_retrieving_book_by_author_and_endyear7(self):
        self.assertEqual(self.booksdatasource.books(author_id=20, end_year=2014), [])

    def test_retrieving_book_by_text1(self):
        self.assertEqual(self.booksdatasource.books(search_text='Mi'),
                         [{'id': 8, 'title': "Leave it to Psmith", 'publication_year': 1923},
                          {'id': 41, 'title': "Middlemarch", 'publication_year': 1871},
                          {'id': 11, 'title': "Midnight's Children", 'publication_year': 1981},
                          {'id': 12, 'title': "Mirror Dance", 'publication_year': 1994}])

    def test_retrieving_book_by_text2(self):
        self.assertEqual(self.booksdatasource.books(search_text='mi'),
                         [{'id': 8, 'title': "Leave it to Psmith", 'publication_year': 1923},
                          {'id': 41, 'title': "Middlemarch", 'publication_year': 1871},
                          {'id': 11, 'title': "Midnight's Children", 'publication_year': 1981},
                          {'id': 12, 'title': "Mirror Dance", 'publication_year': 1994}])

    def test_retrieving_book_by_text3(self):
        self.assertEqual(self.booksdatasource.books(search_text='MI'),
                         [{'id': 8, 'title': "Leave it to Psmith", 'publication_year': 1923},
                          {'id': 41, 'title': "Middlemarch", 'publication_year': 1871},
                          {'id': 11, 'title': "Midnight's Children", 'publication_year': 1981},
                          {'id': 12, 'title': "Mirror Dance", 'publication_year': 1994}])

    def test_retrieving_book_by_multiple_input1(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="All Clear", start_year=2010, end_year=2011),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input2(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="All Clear", start_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input3(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="All Clear"),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input4(self):
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="ar"),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input5(self):  # 5?
        self.assertEqual(self.booksdatasource.books(author_id=0, search_text="AR"),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input6(self):  # 6?
        self.assertEqual(self.booksdatasource.books(author_id=0, end_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010},
                          {'id': 3, 'title': 'Blackout', 'publication_year': 2010},
                          {'id': 27, 'title': 'To Say Nothing of the Dog', 'publication_year': 1997}])

    def test_retrieving_book_by_multiple_input7(self):  # 7?
        self.assertEqual(self.booksdatasource.books(author_id=0, start_year=2010, end_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010},
                          {'id': 3, 'title': 'Blackout', 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input8(self):  # 8
        self.assertEqual(self.booksdatasource.books(author_id=0, start_year=2010, end_year=2011),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010},
                          {'id': 3, 'title': 'Blackout', 'publication_year': 2010}])

    def test_retrieving_book_by_multiple_input9(self):  # 9
        self.assertEqual(self.booksdatasource.books(author_id=0, start_year=2009, end_year=2010),
                         [{'id': 0, 'title': "All Clear", 'publication_year': 2010},
                          {'id': 3, 'title': 'Blackout', 'publication_year': 2010}])

    def test_sorting_book_by_title(self):
        self.assertEqual(self.anotherbooksdatasource.books(sort_by='title'),
                         [{'id': 9, 'title': "Love in the Time of Cholera", 'publication_year': 1985},
                          {'id': 10, 'title': "Main Street", 'publication_year': 1920},
                          {'id': 19, 'title': "Right Ho, Jeeves", 'publication_year': 1934},
                          {'id': 46, 'title': "The Spy Who Came in From the Cold", 'publication_year': 1963}])

    def test_sorting_book_by_year(self):
        self.assertEqual(self.anotherbooksdatasource.books(sort_by='year'),
                         [{'id': 10, 'title': "Main Street", 'publication_year': 1920},
                          {'id': 19, 'title': "Right Ho, Jeeves",'publication_year': 1934},
                          {'id': 46, 'title': "The Spy Who Came in From the Cold", 'publication_year': 1963},
                          {'id': 9, 'title': "Love in the Time of Cholera", 'publication_year': 1985}])




    '''This section contains unit tests for the author(self, author_id) method'''




    def test_retrieving_book_beginning_edge_case(self):
        self.assertEqual(self.booksdatasource.book(0),
                         {'id': 0, 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': 1945,
                          'death_year': None})

    def test_retrieving_book_middle_edge_case1(self):
        self.assertEqual(self.booksdatasource.book(2),
                         {'id': 2, 'last_name': 'Morrison', 'first_name': 'Toni', 'birth_year': 1931,
                          'death_year': None})

    def test_retrieving_book_middle_edge_case1(self):
        self.assertEqual(self.booksdatasource.book(6),
                         {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry', 'birth_year': 1948,
                          'death_year': 2015})

    def test_retrieving_book_end_edge_case(self):
        self.assertEqual(self.booksdatasource.book(24),
                         {'id': 24, 'last_name': 'Carré', 'first_name': 'John', 'birth_year': 1931, 'death_year': None})




    '''This section contains unit tests for the 
        authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year') 
        method
    '''
     
    
    def test_retrieving_author_by_book_id_multiple_authors_edge_case(self):
        self.assertEqual(self.booksdatasource.authors(author_id = 6), [{'id': 5, 'last_name': 'Gaiman', 'first_name': 'Neil',
         'birth_year': 1960, 'death_year': NULL}, {'id': 6, 'last_name': 'Pratchett', 'first_name': 'Terry',
         'birth_year': 1948, 'death_year': 2015}])

    def test_retrieving_author_by_book_id_single_author_edge_case(self):
        self.assertEqual(self.booksdatasource.authors(search_text = 38), [{'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.',
         'birth_year': 1972, 'death_year': NULL}])

    def test_retrieving_author_by_search_text_same_last_name1(self):
        self.assertEqual(self.booksdatasource.authors(search_text = Brontë), [{'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte',
         'birth_year': 1816, 'death_year': 1855}, {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann',
         'birth_year': 1820, 'death_year': 1849}, {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily',
         'birth_year': 1818, 'death_year': 1848}])

    def test_retrieving_author_by_search_text_same_last_name2(self):
        self.assertEqual(self.booksdatasource.authors(search_text = BRontë), [{'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte',
         'birth_year': 1816, 'death_year': 1855}, {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann',
         'birth_year': 1820, 'death_year': 1849}, {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily',
         'birth_year': 1818, 'death_year': 1848}])

    def test_retrieving_author_by_search_text_same_last_name3(self):
        self.assertEqual(self.booksdatasource.authors(search_text = brontë), [{'id': 7, 'last_name': 'Brontë', 'first_name': 'Charlotte',
         'birth_year': 1816, 'death_year': 1855}, {'id': 14, 'last_name': 'Brontë', 'first_name': 'Ann',
         'birth_year': 1820, 'death_year': 1849}, {'id': 15, 'last_name': 'Brontë', 'first_name': 'Emily',
         'birth_year': 1818, 'death_year': 1848}])

    def test_retrieving_author_by_search_text_single_letter(self):
        self.assertEqual(self.booksdatasource.authors(None,k), [{'id': 16, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': NULL}, {'id': 20, 'last_name': 'Jemisen', 'first_name': 'N.K.',
         'birth_year': 1972, 'death_year': NULL}, {'id': 21, 'last_name': 'Jerome', 'first_name': 'Jerome K.',
         'birth_year': 1859, 'death_year': 1927}, {'id': 23, 'last_name': 'Dickens', 'first_name': 'Charles',
         'birth_year': 1812, 'death_year': 1870}])

    def test_retrieving_author_by_start_year_latest_year(self):
        self.assertEqual(booksdatasource.authors(start_year= 1974), [{'id':18, 'last_name': 'Alderman', 'first_name': 'Naomi',
         'birth_year': 1974, 'death_year': NULL}])

    def test_retrieving_author_by_start_year_too_late(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 2000), [])

    def test_retrieving_author_by_start_year_middle_year(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1949), [{'id':5, 'last_name': 'Gaiman', 'first_name': 'Neil',
         'birth_year': 1960, 'death_year': NULL}, {'id':12, 'last_name': 'Bujold', 'first_name': 'McMaster',
         'birth_year': 1949, 'death_year': NULL}, {'id':16, 'last_name': 'Marukami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': NULL}, {'id':18, 'last_name': 'Alderman', 'first_name': 'Naomi',
         'birth_year': 1974, 'death_year': NULL}, {'id':20, 'last_name': 'Jemisen', 'first_name': 'N.K.',
         'birth_year': 1972, 'death_year': NULL}])
        
    def test_retrieving_author_by_end_year_earliest_year(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1775), {'id':4, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817})

    def test_retrieving_author_by_end_year_middle_year(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1820), {'id':4, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}, {'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte',
         'birth_year': 1816, 'death_year': 1855}, {'id':13, 'last_name': 'Melville', 'first_name': 'Herman',
         'birth_year': 1819, 'death_year': 1891}, {'id':14, 'last_name': 'Brontë', 'first_name': 'Ann',
         'birth_year': 1820, 'death_year': 1849}, {'id':15, 'last_name': 'Brontë', 'first_name': 'Emily',
         'birth_year': 1818, 'death_year': 1848}, {'id':22, 'last_name': 'Eliot', 'first_name': 'George',
         'birth_year': 1819, 'death_year': 1880}, {'id':23, 'last_name': 'Dickens', 'first_name': 'Charles',
         'birth_year': 1812, 'death_year': 1870})

    def test_retrieving_author_by_end_year_too_early(self):
        self.assertEqual(self.booksdatasource.authors(end_year = 1700), [])

    def test_retrieving_author_multiple_input1(self):
        self.assertEqual(self.booksdatasource.authors(author_id = 11,start_year = 1930), [{'id':11, 'last_name': 'Rushdie', 'first_name': 'Salman',
         'birth_year': 1947, 'death_year': NULL}])

    def test_retrieving_author_multiple_input2(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1930, end_year = 1950), [{'id':0, 'last_name': 'Willis', 'first_name': 'Connie',
         'birth_year': 1945, 'death_year': NULL}, {'id':2, 'last_name': 'Morrison', 'first_name': 'Toni',
         'birth_year': 1931, 'death_year': NULL}, {'id':6, 'last_name': 'Pratchett', 'first_name': 'Terry',
         'birth_year': 1948, 'death_year': 2015}, {'id':9, 'last_name': 'Márquez', 'first_name': 'Gabriel García',
         'birth_year': 1927, 'death_year': 2014}, {'id':11, 'last_name': 'Rushdie', 'first_name': 'Salman',
         'birth_year': 1947, 'death_year': NULL}, {'id':12, 'last_name': 'Bujold', 'first_name': 'Lois McMaster',
         'birth_year': 1949, 'death_year': NULL}, {'id':16, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': NULL}, {'id':19, 'last_name': 'DuMaurie', 'first_name': 'Daphne',
         'birth_year': 1907, 'death_year': 1989}, {'id':24, 'last_name': 'Carré', 'first_name': 'John Le',
         'birth_year': 1931, 'death_year': NULL}])

    def test_retrieving_author_multiple_input3(self):
        self.assertEqual(self.booksdatasource.authors(author_id = 15, end_year = 1848), [{'id':15, 'last_name': 'Brontë', 'first_name': 'Emily',
         'birth_year': 1818, 'death_year': 1848}])

    def test_retrieving_author_multiple_input4(self):
        self.assertEqual(self.booksdatasource.authors(author_id = 15, start_year = 2000), [])

    def test_retrieving_author_multiple_input5(self):
        elf.assertEqual(self.booksdatasource.authors(end_year =1600), [])

    def test_retrieving_author_multiple_input6(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1774, end_year =1775), [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}])

    def test_retrieving_author_multiple_input7(self):
        self.assertEqual(self.booksdatasource.authors(start_year =  1775, end_year = 1775), [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}])

    def test_retrieving_author_multiple_input8(self):
        self.assertEqual(self.booksdatasource.authors(start_year = 1775, end_year =1776), [{'id':4, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}])

    def test_sort_by_birth_year(self):
        self.assertEqual(self.anotherbooksdatasource.authors(sort_by = 'birth_year'), [{'id':7, 'last_name': 'Brontë', 'first_name': 'Charlotte',
         'birth_year': 1816, 'death_year': 1855}, {'id':13, 'last_name': 'Melville', 'first_name': 'Herman',
         'birth_year': 1819, 'death_year': 1891}, {'id':24, 'last_name': 'Carré', 'first_name': 'John Le',
         'birth_year': 1931, 'death_year': NULL}, {'id':0, 'last_name': 'Willis', 'first_name': 'Connie',
         'birth_year': 1945, 'death_year': NULL}])

if __name__ == '__main__':
    unittest.main()
