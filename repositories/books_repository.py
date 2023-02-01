from db.run_sql import run_sql

from models.authors import Author
from models.books import Book

import repositories.authors_repository as author_repository


def save(book):
    sql = "INSERT INTO books (book_title, genre, authors_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.book_title, book.genre, book.author.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id

    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['authors_id'])
        book = Book(row["book_title"], row["genre"], author, row["id"], )
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['authors_id'])
        book = Book(result["book_title"], result["genre"], author, result["id"])
    return book


def delete(id):
    sql = " DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    sql = "UPDATE books SET (book_title, genre, authors_id) = (%s,%s,%s) WHERE id = %s"
    values = [book.book_title, book.genre, book.author, book.id]
    run_sql(sql, values)


