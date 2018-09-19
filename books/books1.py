#   This is Phase 1 of Books Assignment:
#   @author Charlie Broadbent
#   @author Will Thompson

import sys

#Global Variables 
list_of_books = []
list_of_authors = []
dict_names = {}
dict_books = {}

#Read the file and collect the data form the file.
def read_file(some_file):
    csv_file = open(some_file, 'r')
    
    for line in csv_file:    
        #Check for the case where there are commas within the title:
        if line[0] == '"':
            book = ""
            index = 1
            number_of_commas = 0
            while line[index] != '"':
                book += line[index]
                index += 1
                if line[index] == ",":
                    number_of_commas  += 1
                
            list_of_books.append(book)
            new_line = line.split(",")
            author = new_line[(number_of_commas) + 2]
            
            #Remove the dates from the names: 
            author = remove_birth_dates(author)
            list_of_authors.append(author)
            
        else:
            new_line = line.split(",")
            list_of_books.append(new_line[0])
            
            #Check for multiple authors:
            if "and" in new_line[2]:
            
                #Split both authors into two strings each stored in a list called both_authors:
                both_authors = new_line[2].split("and")
                
                #Delete extra whitespace in the entries list entry left over from the .split("and")
                both_authors[1] = both_authors[1][1 : len(both_authors[1])]  
                both_authors[0] = both_authors[0][0: len(both_authors[0]) - 1] 
                
                #Remove the dates from the names:
                first_author = remove_birth_dates(both_authors[0])
                second_author = remove_birth_dates(both_authors[1])
                          
                #Add authors to list:
                list_of_authors.append(first_author)
                list_of_authors.append(second_author)
                
            else:
                author = new_line[2]
                
                #Remove the dates from the names:
                author = remove_birth_dates(author)
                list_of_authors.append(author)

                
                
                
        

#              These methods print the books or authors depending 
#              on the command line input.





def print_books():
    list_books_no_spaces = refine_book_titles(list_of_books)
    sorted_book_titles = sort(list_books_no_spaces)
    
    if is_reverse():
        for i in range(len(list_books_no_spaces)):
            book_title = sorted_book_titles[len(sorted_book_titles)-1-i]
            print(dict_books[book_title])
    else:
        for i in range(len(list_books_no_spaces)):
            book_title = sorted_book_titles[i]
            print(dict_books[book_title])
          
    
def print_authors():
    list_author_surname = get_authors_last_name(list_of_authors)
    sorted_author_surname = sort(list_author_surname)
    
    if is_reverse():
        for i in range(len(list_author_surname)):
            author_surname = sorted_author_surname[len(sorted_author_surname)-1-i]
            print(dict_names[author_surname])
    else:
        for i in range(len(list_author_surname)):
            author_surname = sorted_author_surname[i]
            print(dict_names[author_surname])
            
            
        
       
#              These methods refine the data collected from the file so that they 
#              may be easily sorted. 




def refine_book_titles(some_list_books):
    list_books_no_spaces = []
    
    for original_book in some_list_books:
        new_book_title = original_book.replace(" ", "")
        list_books_no_spaces.append(new_book_title)
        dict_books[new_book_title] = original_book
    return list_books_no_spaces
    
def remove_birth_dates(name):
    each_name = name.split(" ")
    each_name.remove(each_name[len(each_name) - 1])
    name_without_date = ""
    for i in range(len(each_name)):
        name_without_date += each_name[i] + " "
        
    return name_without_date

    
def get_authors_last_name(some_list_authors):
    list_author_surname = []
   
    for author_full_name in some_list_authors:
        full_name = author_full_name.split(" ")
        
        #remove the dates of the author's birth:
        full_name.remove(full_name[len(full_name) - 1])      
          
        last_name = full_name[len(full_name)-1]        
        list_author_surname.append(last_name)         
        dict_names[last_name] = author_full_name   
        
    return list_author_surname
    
    
    
  
#              These methods check the input on the command line and return certain 
#              boolean values depending on the input.




  
def is_reverse():
    if len(sys.argv) == 4:
        if sys.argv[3] == "reverse":
            return True
    else:
        return False 

def arguments_correct():
    if (len(sys.argv) == 3) or (len(sys.argv) == 4):
        if (sys.argv[2] == "authors") or (sys.argv[2] == "books"):
            return True
    else:
        return False  
        
        
        
#             This section of code contains the instructions for  
#             sorting lists of strings.      


   

#Sorts an input list.
#PRECONDITION: the list must be a list of strings.
def sort(some_list):
    copy_list = some_list.copy()
    sorted_list = []
    for i in range(len(some_list)):
        counter = copy_list[0]

        for j in range(len(copy_list)):
            if compare_words(copy_list[j], counter): #i.e if copy_list[j] comes first
                counter = copy_list[j]
    
        sorted_list.append(counter)
        copy_list.remove(counter)
    return sorted_list
    
#Compares two words and returns true if the first word is the most forward
#lexicographic word
def compare_words(word1, word2):
    
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
    
    
def main():
    
    if arguments_correct():
        read_file(sys.argv[1])
        if sys.argv[2] == "authors":
            print_authors()
        elif sys.argv[2] == "books":
            print_books()
    else:
        print("Usage: python3 books1.py input-file action [sort-direction]", file=sys.stderr)
        
if __name__ == "__main__":
    main()  
    
    
    
