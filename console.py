import pdb
from models.authors import Author
from models.books import Book

import repositories.authors_repository as authors_repository
import repositories.books_repository as books_repository

author_1 = Author("Taylor", "Wood")
authors_repository.save(author_1)
author_2 = Author("Brian", "Wood")
authors_repository.save(author_2)

# authors_repository.select_all()


book_1 = Book("SAS Rogue Heroes", "Fiction", author_1)
books_repository.save(book_1)
book_2 = Book("Saipiens", "Non-Fiction", author_2)
books_repository.save(book_2)


# result = authors_repository.delete(4)

# books_repository.select_all()

# book_3 = Book("RANGERS","RANGERS", 22)
# books_repository.update(book_3)

# author_3 = Author("TAYLOR", "TAYLOR", )
# authors_repository.update(author_3)

books_repository.select_all()