from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from schemas.user_schema import user_schema, users_schema
from datetime import date

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/api/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    result = users_schema.dump(users)
    return jsonify(result)

@user_blueprint.route('/api/user/<int:id>', methods=['GET'])
def get_user_by_id(id):
    user = User.query.get(id)
    result = user_schema.dump(user)
    return jsonify(result);

@user_blueprint.route('/api/user', methods=['POST'])
def add_user():
    auth_id = request.json['auth_id']
    email = request.json['email']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    dob = date.fromisoformat(request.json['dob'])
    bio = request.json['bio']
    city = request.json['city']
    state = request.json['state']
    country = request.json['country']
    is_profile_public = request.json['is_profile_public']
    
    new_user = User(auth_id, email, first_name, last_name, dob, bio, city, state, country, True, is_profile_public)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)

@user_blueprint.route('/api/user/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if 'email' in request.json:
        user.email = request.json['email']
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
    if 'is_profile_public' in request.json:
        user.is_profile_public = request.json['is_profile_public']
    
    db.session.commit()
    return user_schema.jsonify(user)
