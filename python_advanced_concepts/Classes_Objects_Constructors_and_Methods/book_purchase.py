"""
Create a class Book with a parameterised constructor then takes name_of_book, author,
year_of_publish, price_of_book, no_of_copies_available. Create the following methods -
- order_book(no_of_books) : This method should return price of purchase, if no of
books is less than or equal to no_of_copies_available. Else, return “No stock”.
- add_quantity(is_admin, quantity): This method should add quantity of books (2nd
param) to existing no_of_copies_available if is_admin is True and return “Book
quantity updated as <<count>>” . If is_admin is False, return “Unauthorised” as
output.

Sample Input/Output:
book = Book(“Software Quality Assurance”, “Mr.Jochen”, 1994, 100, 10)

book.order_book(10)            1000                       10*100 = 1000
book.order_book(1000)          No stock
book.order_book(1)             100                        1*100 = 100
book.order_book(43)            No stock
book.add_quantity(False, 100)  Unauthorized
book.add_quantity(True, 31)     Book quantity updated as 41
"""

class Book:
    def __init__(self,name_of_book, author, year_of_publish, price_of_book, no_of_copies_available):
        self.name_of_book = name_of_book
        self.author = author
        self.year_of_publish = year_of_publish
        self.price_of_book = price_of_book
        self.no_of_copies_available = no_of_copies_available

    def order_book(self, no_of_books):
        if no_of_books <= self.no_of_copies_available:
            return no_of_books*self.price_of_book
        else:
            return "No stock"

    def add_quantity(self, is_admin, quantity):
        if is_admin:
            self.no_of_copies_available += quantity
            return "Book quantity updated as "+ str(self.no_of_copies_available)
        else:
            return 'Unauthorised'

book = Book('Software Quality Assurance', 'Mr.Jochen', 1994, 100, 10)

print(book.order_book(10))           
print(book.order_book(1000))         
print(book.order_book(1))             
print(book.order_book(43))
print(book.add_quantity(False, 100))

print(book.add_quantity(True, 31))


"""
OUTPUT
------

1000
No stock
100
No stock
Unauthorised
Book quantity updated as 41
"""

