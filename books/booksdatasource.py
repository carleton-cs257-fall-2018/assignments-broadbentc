#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class, Fall 2018.
'''

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).

    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.

    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871
                    

                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6
                  
                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''

        self.book_list = self.read_books_file(books_filename)
        self.author_list = self.read_authors_file(authors_filename)
        self.book_author_link_dict = self.read_books_authors_link_file(books_authors_link_filename)

    def read_books_file(self, some_file):

        book_csv_file = open(some_file, 'r', encoding='utf-8')
        list_of_books_from_datasource = []

        for line in book_csv_file:
            no_commas = True
            index = 0

            #Check for title with commas
            while line[index] != ',':
                index += 1
            if line[index + 1] == '"':
                no_commas = False

            #Adding normal title (no commas in title)
            if no_commas == True:
                book_info = line.split(",")
                book_id = book_info[0]
                book_title = book_info[1]
                book_date = book_info[2]
                book_dict = {'id' : book_id, 'title': book_title, 'publication_year': book_date}
                list_of_books_from_datasource.append(book_dict)

            #Adding title with commas
            else:
                book_info = line.split('"')
                book_title = book_info[1]
                book_info.pop(1)
                book_id = book_info[0].replace(',', "")
                book_date = book_info[1].replace(',', "")
                book_dict = {'id': book_id, 'title': book_title, 'publication_year': book_date}
                list_of_books_from_datasource.append(book_dict)

        return list_of_books_from_datasource

    def read_authors_file(self, some_file):

        authors_csv_file = open(some_file, 'r', encoding='utf-8')
        authors_list = []

        for line in authors_csv_file:
            author_info = line.split(',')
            author_id = author_info[0]
            author_last_name = author_info[1]
            author_first_name = author_info[2]
            author_birth_year = author_info[3]

            if author_info[4] == 'NULL': #Is NULL a string?
                author_death_year = "None"
            else:
                author_death_year = author_info[4]
            author_dict = {'id': author_id, 'last_name': author_last_name, 'first_name': author_first_name,
         'birth_year': author_birth_year, 'death_year': author_death_year}

            authors_list.append(author_dict)

        return authors_list

    def read_books_authors_link_file(self, some_file):

        books_authors_link_csv_file = open(some_file, 'r', encoding='utf-8')
        books_authors_link_dict = {}

        for line in books_authors_link_csv_file:
            link_info = line.split(',')
            book_id = link_info[0]
            author_id = link_info[1]
            if author_id not in books_authors_link_dict.keys():
                books_authors_link_dict[author_id] = [book_id]
            else:
                books_authors_link_dict[author_id].append(book_id)

        return books_authors_link_dict


    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''
    
        for book in self.book_list:
            if book['id'] == book_id:
                return book
            else:
                print("There is no book with id: " + book_id + "in the data source!")

    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
                
            See the BooksDataSource comment for a description of how a book is represented.
        '''
        
        #self.book_list 
        #self.author_list 
        #self.book_author_link_dict
        
        refined_list_of_books = []
        sorted_refined_list_of_books = []
        add_book_author_id = True
        add_book_search_text = True
        add_book_start_year = True
        add_book_end_year = True
        
        for book in self.book_list:
            
            #Check author_id
            if author_id != None:
                book_author_id = book_author_link_dict[book['id']]
                if author_id == book_author_id:
                    add_book_author_id = True
                else:
                    add_book_author_id = False
            
            #Check search_text
            if search_text != None:
                desired_text = search_text.lower()
                copy_of_book = book['title'].lower()
                
                if desired_text in copy_of_book:
                    add_book_search_text = True
                else:
                    add_book_search_text = False
                    
            #Check start_year
            if start_year != None:
                book_start_year = book['publication_year']
                if start_year <= book_start_year:
                    add_book_start_year = True
                else:
                    add_book_start_year = False
                    
            #Check end_year
            if end_year != None:
                book_end_year = book['publication_year']
                if end_year >= book_end_year:
                    add_book_end_year = True
                else:
                    add_book_end_year = False
                    
            if ((add_book_author_id) and (add_book_search_text) and (add_book_start_year) and (add_book_end_year)):
                refined_list_of_books.append(book)
            
            #Sort the refined_list_of_books
            if sort_by == 'year':
                sorted_refined_list_of_books = self.sort_by_publication_year(refined_list_of_books)
                return sorted_refined_list_of_books
                
            else:            
                sorted_refined_list_of_books = self.sort_by_title(refined_list_of_books)
                return sorted_refined_list_of_books
                
            

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.) '''
        return {}

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year
        
            See the BooksDataSource comment for a description of how an author is represented.
        '''
        pass


    # Note for my students: The following two methods provide no new functionality beyond
    # what the books(...) and authors(...) methods already provide. But they do represent a
    # category of methods known as "convenience methods". That is, they provide very simple
    # interfaces for a couple very common operations.
    #
    # A question for you: do you think it's worth creating and then maintaining these
    # particular convenience methods? Is books_for_author(17) better than books(author_id=17)?

    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)
    
    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.authors(book_id=book_id)
        
        
        
        
        
        
        
        
        
    def sort_by_publication_year(self, some_list):
        copy_list = some_list.copy()
        sorted_list = []
        for i in range(len(some_list)):
            counter = copy_list[0]

            for j in range(len(copy_list)):
                if copy_list[j]['publication_year'] < counter['publication_year']: 
                    counter = copy_list[j]
    
            sorted_list.append(counter)
            copy_list.remove(counter)
        return sorted_list

    def sort_by_title(self, some_list):
        copy_list = some_list.copy()
        sorted_list = []
        for i in range(len(some_list)):
            counter = copy_list[0]

            for j in range(len(copy_list)):
                if self.compare_words(copy_list[j]['title'], counter['title']): #i.e if copy_list[j] comes first
                    counter = copy_list[j]
    
            sorted_list.append(counter)
            copy_list.remove(counter)
        return sorted_list
    
    '''Compares two words and returns true if the first word is the most forward
       lexicographic word'''
    def compare_words(self, word1, word2):
    
        new_word1 = word1.lower()
        new_word2 = word2.lower()
    
        list1 = []
        list2 = []
    
        for char in new_word1:
            list1.append(ord(char))
        for char in new_word2:
            list2.append(ord(char))
    
        if len(word1) <= len(new_word2):
            shortest_length = len(new_word1)
            shorter_word = True
        else:
            shortest_length = len(new_word2)
            shorter_word = False
    
        for i in range(shortest_length):
            if list1[i] < list2[i]:
                return True 
            if list1[i] > list2[i]:
                return False
        return shorter_word
