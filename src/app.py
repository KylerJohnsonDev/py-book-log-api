#Import required packages
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# https://tutorialwithproject.com/flask-rest-api-crud-operations/

# Init app
app = Flask(__name__)

# SqlAlchemy
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/kylerjohnson/databases/book_inventory/book_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True 
db = SQLAlchemy(app)
ma = Marshmallow(app)

# models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    auth_id = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    dob = db.Column(db.Date)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country = db.Column(db.String)
    is_active = db.Column(db.Boolean)
    
    def __init__(self, id, auth_id, first_name, last_name, dob, bio, city, state, country, is_active):
        self.id = id
        self.auth_id = auth_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.bio = bio
        self.city = city
        self.state = state
        self.country = country
        self.is_active = is_active
        
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'auth_id', 'first_name', 'last_name', 'dob', 'bio', 'city', 'state', 'country', 'is_active')
        

user_schema = UserSchema()
users_schema = UserSchema(many=True)
    
#Create a Hello-World route
@app.route('/health', methods=['GET'])
def get_hello_world():
    return jsonify({'status': 'Healthy'})

@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

@app.route('/api/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    result = user_schema.dump(user)
    return jsonify(result);

@app.route('/api/user', methods=['POST'])
def add_user():
    user = User

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
