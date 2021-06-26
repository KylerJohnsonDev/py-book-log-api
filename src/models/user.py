from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auth_id = db.Column(db.String)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    is_profile_public = db.Column(db.Boolean)
    
    def __init__(self, auth_id, email, first_name, last_name, dob, bio, city, state, country, is_active, is_profile_public):
        self.auth_id = auth_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.bio = bio
        self.city = city
        self.state = state
        self.country = country
        self.is_active = is_active
        self.is_profile_public = is_profile_public