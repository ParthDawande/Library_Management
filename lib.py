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
        
        
        
class Library:
    def __init__(self):
        self.books = []