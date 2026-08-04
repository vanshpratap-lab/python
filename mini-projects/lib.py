class library:
    def __init__(self,books):
        self.books = books
        self.no_of_books = len[books]

    def show_all_books(self):
        print("books in the library:")
        for book in self.books:
            print("-", book)

    def show_one_book(self,index):
        print(self.books[index])

    def get_no_of_books(self):
        return self.no_of_books

lib = ["harry potter", "the social network", "the wolf of wall street", "the founder"]

lib.show_all_books()
print()

lib.show_one_book(1)
print

count = lib.get_no_of_books
print(f"total no. of book is {count}")

lib.books.append("a new book")
lib.no_of_books = len(lib.books)
print(f"\nafter adding a book (still same run)")
lib.show_all_books()
print(f"\ntotal no. of books : {lib.get_no_of_books()}")
