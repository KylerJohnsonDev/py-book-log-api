#Import required packages
from flask import Flask, request, jsonify
from datetime import date
from extensions import db, ma
from models.user import User

# https://tutorialwithproject.com/flask-rest-api-crud-operations/

# Init app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/kylerjohnson/databases/book_inventory/book_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

db.init_app(app)
        
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
    auth_id = request.json['auth_id']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    dob = date.fromisoformat(request.json['dob'])
    bio = request.json['bio']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    
    new_user = User(auth_id, first_name, last_name, dob, bio, city, state, country, True)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@app.route('/api/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if 'first_name' in request.json:
        user.first_name = request.json['first_name']
    if 'last_name' in request.json:
        user.last_name = request.json['last_name'] or user.last_name
    if 'bio' in request.json:
        user.bio = request.json['bio'] or user.bio
    if 'city' in request.json:
        user.city = request.json['city'] or user.city
    if 'state' in request.json:
        user.state = request.json['state'] or user.state
    if 'country' in request.json:
        user.country = request.json['country'] or user.country
    if 'is_active' in request.json:
        user.is_active = request.json['is_active'] or user.is_active
    
    db.session.commit()
    return user_schema.jsonify(user)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
