from extensions import ma

class Book_Schema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'genre_id', 'genre')
        

book_schema = Book_Schema()
books_schema = Book_Schema(many=True)