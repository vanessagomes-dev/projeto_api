# routes/users.py

# routes/users.py
from flask import Blueprint, jsonify, request
from models.user import User # type: ignore

# Blueprints permitem que você divida sua aplicação Flask em componentes modulares e reutilizáveis.
users_bp = Blueprint('users_bp', __name__) 

users = [
    {'id': 1, 'name': 'Vanessa'},
    {'id': 2, 'name': 'Alexandre'}
]

@users_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@users_bp.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    if not new_user or 'id' not in new_user or 'name' not in new_user:
        return jsonify({'message': 'Invalid data'}), 400
    users.append(new_user)
    return jsonify(new_user), 201

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    user['name'] = data.get('name', user['name'])
    return jsonify(user)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'})
