class Book:
    def __init__(self, title, author):
        self.title = title          
        self.author = author                
        self._is_checked_out = False        

    def is_available(self):
        return not self._is_checked_out

    def check_out(self):
        if self._is_checked_out:
            return False  
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False  
        self._is_checked_out = False
        return True


class Library:
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f'Book "{title}" has been checked out.'
                else:
                    return f'Book "{title}" is already checked out.'
        return f'Book "{title}" not found in the library.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_back():
                    return f'Book "{title}" has been returned.'
                else:
                    return f'Book "{title}" was not checked out.'
        return f'Book "{title}" not found in the library.'

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not avaclass Book:
    def __init__(self, title, author):
        self.title = title                  # public attribute
        self.author = author                # public attribute
        self._is_checked_out = False        # private attribute to track availability

    def is_available(self):
        return not self._is_checked_out

    def check_out(self):
        if self._is_checked_out:
            return False  # Already checked out
        self._is_checked_out = True
        return True

    def return_back(self):
        if not self._is_checked_out:
            return False  # Not checked out yet
        self._is_checked_out = False
        return True


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f'Book "{title}" has been checked out.'
                else:
                    return f'Book "{title}" is already checked out.'
        return f'Book "{title}" not found in the library.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_back():
                    return f'Book "{title}" has been returned.'
                else:
                    return f'Book "{title}" was not checked out.'
        return f'Book "{title}" not found in the library.'

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            return "No books available."
        return "\n".join(f'"{book.title}" by {book.author}' for book in available_books)


# Example usage:
if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    print(library.list_available_books())
    print(library.check_out_book("1984"))
    print(library.list_available_books())
    print(library.return_book("1984"))
    print(library.list_available_books())ilable_books:
            return "No books available."
        return "\n".join(f'"{book.title}" by {book.author}' for book in available_books)


# Example usage:
if __name__ == "__main__":
    library = Library()

    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    print(library.list_available_books())
    print(library.check_out_book("1984"))
    print(library.list_available_books())
    print(library.return_book("1984"))
    print(library.list_available_books())
