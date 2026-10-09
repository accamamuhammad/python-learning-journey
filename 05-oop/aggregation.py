# Aggregation
# Represents a relationship where one object (the whole)
# contains references to one or more INDEPENDENT objects (the parts)

class Libary:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f'{book.title} by {book.author} ' for book in self.books]
  
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

libary = Libary('Abuja Open Libary')

book1 = Book('Harry Potter', 'J.K Rowling')
book2 = Book('The Hobbit', 'R.R Tolkein')
book3 = Book('Life', 'Naira Marley')

libary.add_book(book1)
libary.add_book(book2)
libary.add_book(book3)

print(libary.name)
for book in libary.list_books():
    print(book)
