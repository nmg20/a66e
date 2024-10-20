# backend/app/models/Playlist.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Playlist(db.Model):
    __tablename__ = 'playlists'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    title = db.Column(db.String(200), nullable=False)  # Título de la playlist
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # ID del usuario que posee la playlist

    def __repr__(self):
        return f'<Playlist {self.title}>'
