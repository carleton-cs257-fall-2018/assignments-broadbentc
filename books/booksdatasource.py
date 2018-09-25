'''
    booksdatasource.py
    @author Will Thompson
    @author Charlie Broadbent
    CS 257 Software Design class, Fall 2018.
'''

import csv

class BooksDataSource:
    '''

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

        self.book_list = self.set_book_list(books_filename)
        self.author_list = self.set_author_list(authors_filename)
        self.book_to_author_dict, self.author_to_book_dict  = self.set_book_and_author_dicts(books_authors_link_filename)

    def set_book_list(self, csv_file):
        
        books_from_file = []
        with open(csv_file, newline = '') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            
            for row in csv_reader:
                book_id = int(row[0])
                book_title = row[1]
                publication_year = int(row[2])
                
                book = {'id' : book_id, 'title' : book_title, "publication_year" : publication_year}
                books_from_file.append(book)
        
        return books_from_file

    def set_author_list(self, csv_file):
        
        authors_from_file = []
        with open(csv_file, newline = '') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            
            for row in csv_reader:
                author_id = int(row[0])
                author_last_name = row[1]
                author_first_name = row[2]
                author_birth_year = int(row[3])
                author_death_year = row[4]
                
                if author_death_year != 'NULL':
                    author_death_year = int(author_death_year)
                    
                
                author = {'id' :author_id, 'last_name' : author_last_name, 'first_name' : author_first_name, 'birth_year' : author_birth_year, 'death_year' : author_death_year}
                authors_from_file.append(author)
        
        return authors_from_file
        
    def set_book_and_author_dicts(self, csv_file):
    
        book_to_author_from_file = {}
        author_to_book_from_file = {}
        
        with open(csv_file, newline = '') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            
            for row in csv_reader:
                book_id = int(row[0])
                author_id = int(row[1])            
                
                book_to_author_from_file[book_id] = author_id
                
                if author_id not in author_to_book_from_file.keys():
                    author_to_book_from_file[author_id] = [book_id]
                else:
                    author_to_book_from_file[author_id].append(book_id)
                    
        return book_to_author_from_file, author_to_book_from_file

    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.) '''
    
        for book in self.book_list:
            if book['id'] == int(book_id):
                return book
        
        print("There is no book with id: " + str(book_id) + " in the data source!")

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
        
        refined_list_of_books = []
        sorted_refined_list_of_books = []
        add_book_author_id = True
        add_book_search_text = True
        add_book_start_year = True
        add_book_end_year = True
        
        for book in self.book_list:
            
            #Check author_id
            if author_id != None:
                book_author_id = self.book_to_author_dict[book['id']]
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
                sorted_refined_list_of_books = self.sort_by_year(refined_list_of_books, 'publication_year')
            else:            
                sorted_refined_list_of_books = self.sort_by_title_or_name(refined_list_of_books, 'title')
            
        return sorted_refined_list_of_books
                
            

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.) '''
        
        for author in self.author_list:
            if author['id'] == int(author_id):
                return author
            
        print("There is no author with id: " + str(author_id) + " in the data source!")

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
        
        
        refined_list_of_authors = []
        sorted_refined_list_of_authors = []
        add_author_book_id = True
        add_author_search_text = True
        add_author_birth_year = True
        add_author_death_year = True
        
        for author in self.author_list:
            
            #Check book_id
            if book_id != None:
                author_book_id = self.author_to_book_dict[author['id']]
                if book_id == author_book_id:
                    add_author_book_id = True
                else:
                    add_author_book_id = False
            
            #Check search_text
            if search_text != None:
                desired_text = search_text.lower()
                copy_of_author_first_name = author['first_name'].lower()
                copy_of_author_last_name = author['last_name'].lower()
                
                if (desired_text in copy_of_author_first_name) or (desired_text in copy_of_author_last_name):
                    add_author_search_text = True
                else:
                    add_author_search_text = False
                    
             
            author_birth_year = author['birth_year']
            author_death_year = author['death_year'] 
                   
            #Check start_year
            if start_year != None:
                if start_year <= author_birth_year:
                    add_author_birth_year = True
                    
                if author_death_year == 'NULL':
                    add_author_birth_year = True
                
                if author_death_year != 'NULL':
                    if start_year <= author_death_year:
                        add_author_birth_year = True               
                else:
                    add_author_birth_year = False
                    
            #Check end_year
            if end_year != None:
                if  author_death_year <= end_year:
                    add_author_death_year = True
                    
                if author_birth_year <= end_year:
                    add_author_death_year = True
                
                else:
                    add_author_death_year = False
                    
            if ((add_author_book_id) and (add_author_search_text) and (add_author_birth_year) and (add_author_death_year)):
                
                refined_list_of_authors.append(author)
            
            #Sort the refined_list_of_books
            if sort_by == 'birth_year':
                sorted_refined_list_of_authors = self.sort_by_year(refined_list_of_authors, 'birth_year')
            else:            
                sorted_refined_list_of_authors = self.sort_by_title_or_name(refined_list_of_authors, 'last_name')
            
        return sorted_refined_list_of_authors     
        
    
    
    #Convenience Methods:
    def books_for_author(self, author_id):
        ''' Returns a list of all the books written by the author with the specified author ID.
            See the BooksDataSource comment for a description of how an book is represented. '''
        return self.books(author_id=author_id)
    
    def authors_for_book(self, book_id):
        ''' Returns a list of all the authors of the book with the specified book ID.
            See the BooksDataSource comment for a description of how an author is represented. '''
        return self.authors(book_id=book_id)
              
    
    
    
    #Helper Methods: 
    def sort_by_year(self, some_list, year_type ):
        copy_list = some_list.copy()
        sorted_list = []
        for i in range(len(some_list)):
            counter = copy_list[0]

            for j in range(len(copy_list)):
                if copy_list[j][year_type] < counter[year_type]: 
                    counter = copy_list[j]
    
            sorted_list.append(counter)
            copy_list.remove(counter)
        return sorted_list

    def sort_by_title_or_name(self, some_list, name):
        copy_list = some_list.copy()
        sorted_list = []
        for i in range(len(some_list)):
            counter = copy_list[0]

            for j in range(len(copy_list)):
                if self.compare_words(copy_list[j][name], counter[name]): 
                    counter = copy_list[j]
    
            sorted_list.append(counter)
            copy_list.remove(counter)
        return sorted_list
    
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
