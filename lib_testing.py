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

if __name__ == '__main__':
    unittest.main()