from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from extensions import db

class Genre(db.Model):
    __tablename__= 'genres'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    
    book_id = db.Column(db.Integer, ForeignKey('books.id'))
    books = relationship('Book', back_populates='genres', uselist=False)
    