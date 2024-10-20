from flask import Blueprint, jsonify

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de la aplicación."})
