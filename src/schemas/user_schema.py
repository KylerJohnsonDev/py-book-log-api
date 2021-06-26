from extensions import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'auth_id', 'email', 'first_name', 'last_name', 'dob', 'bio', 'city', 'state', 'country', 'is_active', 'is_profile_public')
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)