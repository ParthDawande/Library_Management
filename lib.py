class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Year: {self.year}"
    
class Library:
    def __init__(self):
        self.books = []