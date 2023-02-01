from flask import Flask, render_template, request, redirect

from flask import Blueprint

from repositories import authors_repository
from repositories import books_repository
from models.authors import Author
from models.books import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def tasks():
    books = books_repository.select_all()
    
    return render_template("books/index.html", book_list=books)

