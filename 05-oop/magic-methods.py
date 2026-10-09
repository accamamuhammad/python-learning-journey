# Magic methods = Dunder methods (__init__, __str__, __eq__, etc.) automatically called by built-in Python operations

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title

    def __getitem__(self, key):
        if key == 'kal':
            return self.title

book1 = Book('Kal ho na ho', 'Sharul Khan', 666)
book2 = Book('Kuch Kuch hota', 'Sharul Khan', 969)
book3 = Book('Full metal alchemist', 'Shamo don', 31)

print(book1['kal'])
