from flask_sqlalchemy import SQLAlchemy
from app.models import db

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    username = db.Column(db.String(80), unique=True, nullable=False)  # Nombre de usuario
    email = db.Column(db.String(120), unique=True, nullable=False)
    playlists = db.relationship('Playlist', back_populates='owner')  # Relación con playlists

    def __repr__(self):
        return f'<User {self.username}>'