from flask import Blueprint, jsonify, request
from extensions import db
from models.book_entry import Book_Entry
from models.book import Book
from schemas.book_entry_schema import book_entry_schema, book_entries_schema
from schemas.book_schema import Book_Schema

book_entries_blueprint = Blueprint('book_entries_blueprint', __name__)

@book_entries_blueprint.route('/api/book-entries', methods=['GET'])
def get_all_book_entries():
    book_entries = Book_Entry.query.all()
    result = book_entries_schema.dump(book_entries)
    return jsonify(result)

@book_entries_blueprint.route('/api/book-entry', methods=['POST'])
def add_book_entry():
    user_id = request.json['user_id']
    has_read = request.json['has_read']
    notes = request.json['notes']
    book_title = request.json['book_title']
    book_author = request.json['book_author']
    book_genre_id = request.json['book_genre_id']
    
    book = Book(book_title, book_author, book_genre_id)
    
    db.session.add(book)
    db.session.commit()
    print('book saved with id of {}'.format(book.id))
    
    book_entry = Book_Entry(user_id, has_read, notes, book.id)
    db.session.add(book_entry)
    db.session.commit()
    
    book.book_entry_id = book_entry.id
    db.session.commit()
    
    result = book_entry_schema.dump(book_entry)
    return jsonify(result)