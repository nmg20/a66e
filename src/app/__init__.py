from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db
from .routes.main_routes import main_routes
from .routes.UserController import user_controller
from .routes.SpotifyController import spotify_controller

# Inicializar la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mycelium.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la base de datos con la app
    db.init_app(app)

    # Importar aquí para evitar importaciones circulares
    with app.app_context():
        app.register_blueprint(user_controller)

    with app.app_context():
        app.register_blueprint(spotify_controller)

    return app
