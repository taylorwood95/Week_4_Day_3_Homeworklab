class Book:

    def __init__(self, book_title, genre, author, id =  None):
        self.id = id
        self.book_title = book_title
        self.genre = genre
        self.author = author