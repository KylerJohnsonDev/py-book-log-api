from extensions import ma

class Genre_Schema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'is_active')
        

genre_schema = Genre_Schema()
genres_schema = Genre_Schema(many=True)