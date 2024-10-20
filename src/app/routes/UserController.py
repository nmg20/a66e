from flask import Blueprint, request, jsonify
from app.models.user import UserService

user_controller = Blueprint('user_controller',__name__)

@user_controller.route('/user', methods=['POST'])
def register_user():
    data = reqest.json
    user = UserService.register_user(data['username'], data['email'])
    return jsonify(
        {
        'id': user.id,
        'username': user.username,
        'email': user.email
        }), 201

@user_controller.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = UserService.get_user(id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
            }), 201
    else:
        return jsonify({"error": "User not found"}), 404

@user_controller.route('/')
def home():
    # return jsonify({"message": "Bienvenido a la API de la aplicación."})
    return "Holii:)"