from flask import Blueprint, jsonify, request
from extensions import db
from models.book import Book
from schemas.book_schema import book_schema, books_schema

book_blueprint = Blueprint('book_blueprint', __name__)

@book_blueprint.route('/api/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    result = book_schema.dump(books)
    return jsonify(result)

@book_blueprint.route('/api/book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    genre_id = request.json['genre_id']
    
    book = Book(title, author, genre_id)