class User:
    def __init__(self, username, preferences=None):
        self.username = username
        self.playlists = []
        self.preferences = preferences or UserPreferences()

    def create_playlist(self, name):
        playlist = Playlist(name)
        self.playlists.append(playlist)
        return playlist

    def delete_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)

    def set_preferences(self, preferences):
        self.preferences = preferences

    def __repr__(self):
        return f"User(username={self.username}, playlists={len(self.playlists)})"