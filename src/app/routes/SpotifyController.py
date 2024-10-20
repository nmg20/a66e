from flask import Blueprint, jsonify
from app.services.SpotifyService import SpotifyService

spotify_controller = Blueprint('spotify_controller',__name__)
spotify_servie = SpotifyService()

@spotify_controller.route('/playlists')
def list_playlists():
    playlists = spotify_servie.list_playlists()
    return jsonify(playlists)