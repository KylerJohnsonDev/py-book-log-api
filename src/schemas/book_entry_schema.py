from extensions import ma

class Book_Entry_Schema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'book_id', 'has_read', 'notes', 'book')
        
book_entry_schema = Book_Entry_Schema()
book_entries_schema = Book_Entry_Schema(many=True)