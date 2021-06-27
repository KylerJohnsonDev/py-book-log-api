from flask.blueprints import Blueprint
from flask.json import jsonify
from extensions import db
from models.book_entry import Book_Entry
from schemas.book_entry_schema import book_entry_schema, book_entries_schema

book_entries_blueprint = Blueprint('book_entries_blueprint', __name__)

@book_entries_blueprint.route('/api/book-entries', methods=['GET'])
def get_all_book_entries():
    book_entries = Book_Entry.query.all()
    result = book_entries_schema.dump(book_entries)
    return jsonify(result)