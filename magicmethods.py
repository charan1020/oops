#magic methods are special methods in Python that start and end with double underscores (__).
#They allow you to define how objects of a class behave with built-in operations and functions.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages
    def __lt__(self, other):
        return self.pages < other.pages
    def __gt__(self, other):
        return self.pages > other.pages
    def __add__(self, other):
        return f"{self.pages + other.pages} pages"
    def __contains__(self, item):
        return item in self.title or item in self.author
book1 = Book("1984", "George Orwell", 328)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book3 = Book("Harry Potter", "J.K. Rowling", 309)
print(book1 == book2)
print(book1)
print(len(book3))
print(book1 < book2)
print(book1 > book3)
print(book2 + book3)
print("Harry" in book3)
print("Orwell" in book1)