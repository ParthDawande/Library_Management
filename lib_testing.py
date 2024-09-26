import unittest
from lib import Library, Book

class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Set up the library and a sample book before each test."""
        self.library = Library()
        self.book1 = Book("123", "Test-Driven Development", "Kent Beck", 2002)
        self.book2 = Book("456", "Refactoring", "Martin Fowler", 1999)
    
    def test_add_book(self):
        """Test if books can be added to the library."""
        self.library.add_book(self.book1)
        self.assertIn(self.book1, self.library.books)
        self.assertEqual(len(self.library.books), 1)
        
    def test_borrow_book(self):
        """Test if a book can be borrowed from the library."""
        self.library.add_book(self.book1)
        borrowed_book = self.library.borrow_book("123")
        self.assertEqual(borrowed_book, self.book1)
        self.assertNotIn(self.book1, self.library.books)
        self.assertEqual(len(self.library.books), 0)
        
    def test_return_book(self):
        """Test if a borrowed book can be returned to the library."""
        self.library.add_book(self.book1)
        self.library.borrow_book("123")
        self.library.return_book(self.book1)
        self.assertIn(self.book1, self.library.books)
        self.assertEqual(len(self.library.books), 1)
        
    

if __name__ == '__main__':
    unittest.main()