
class Book:
    #Represents a book with a title, author, and availability status.
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        #Marks the book as checked out if it is available.
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        #Marks the book as available if it is checked out.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        #Returns True if the book is available, False otherwise.
        return not self._is_checked_out


class Library:
    #Represents a library containing a collection of books.
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        #Adds a book to the library's collection.
        self._books.append(book)

    def check_out_book(self, title):
        #Checks out a book by title if it is available.
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}' successfully.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        #Returns a book by title if it was checked out.
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}' successfully.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        #Prints all available books in the library.
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No books available.")
