from extensions import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.book import Book

class Book_Entry(db.Model):
    __tablename__= 'book_entries'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    book_id = db.Column(db.Integer, ForeignKey('book.id'))
    has_read = db.Column(db.Boolean)
    notes = db.Column(db.String)
    book = relationship('Book', back_populates="book_entries", uselist=False)
    
    def __init__(self, user_id, has_read, notes, book_id):
        self.user_id = user_id
        self.has_read = has_read
        self.notes = notes
        self.book_id = book_id
    
    
    