# Challenge: Library And Books(OOP):

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True   # default availability


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []   # store multiple books in a list
    
    def add_book(self, book):
        """Add a new book to the library."""
        self.books.append(book)
        print(f'Added "{book.title}" by {book.author} to {self.name}')
    
    def borrow_book(self, title):
        """Borrow a book by title if available."""
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print(f'You borrowed "{book.title}"')
                return
        print(f'Sorry, "{title}" is not available right now.')
    
    def return_book(self, title):
        """Return a borrowed book."""
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                print(f'You returned "{book.title}"')
                return
        print(f'"{title}" was not borrowed from {self.name}.')
    
    def show_books(self):
        """Display all books and their status."""
        print(f"\nBooks in {self.name}:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(f'- "{book.title}" by {book.author} [{status}]')

# Create books
book1 = Book("1984", "George Orwell")
book2 = Book("Atomic Habits", "James Clear")

# Create a library
my_library = Library("City Library")

# Add books
my_library.add_book(book1)
my_library.add_book(book2)

# Borrow a book
my_library.borrow_book("1984")

# Show library status
my_library.show_books()

# Return the book
my_library.return_book("1984")
my_library.show_books()