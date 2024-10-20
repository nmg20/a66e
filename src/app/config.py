from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

class Config:

    ##### Spotify #####
    SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
    SPOTIFY_USERNAME = os.getenv('SPOTIFY_USERNAME')