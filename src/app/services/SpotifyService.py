import spotipy
from spotipy.oauth2 import SpotifyOAuth
from app.config import Config

class SpotifyService:
    def __init__(self):
        self.spotify = spotipy.Spotify(
            auth_manager = SpotifyOAuth(
                client_id = Config.SPOTIFY_CLIENT_ID,
                client_secret = Config.SPOTIFY_CLIENT_SECRET,
                redirect_uri=Config.SPOTIFY_REDIRECT_URI,
                scope='user-library-read'))

    def list_playlists(self):
        return self.spotify.current_user_playlists()