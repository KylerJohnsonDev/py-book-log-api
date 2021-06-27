from extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from models.genre import Genre

class Book(db.Model):
    __tablename__= 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    genre_id = db.Column(db.Integer, ForeignKey('genre.id'))
    genres = relationship('Genre', back_populates="books", uselist=False)
    book_entry_id = db.Column(db.Integer, ForeignKey('book_entries.id'))
    book_entries = relationship('Book_Entry', back_populates='book', uselist=False)
    
    def __init__(self, title, author, genre_id, book_entry_id):
        self.title = title
        self.author = author
        self.genre_id = genre_id
        self.book_entry_id = book_entry_id