class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
    def add_book(self, book):
        """Adds a new book to the library."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    
    def borrow_book(self, isbn):
        """Borrows a book from the library by its ISBN."""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"You have borrowed '{book.title}'.")
                return book
        print(f"Book with ISBN {isbn} is not available.")
        return None
    
    def return_book(self, book):
        """Returns a book to the library."""
        
        
        
class Library:
    def __init__(self):
        self.books = []