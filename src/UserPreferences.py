class UserPreferences:
    def __init__(self, download_location, audio_format, quality):
        self.download_location = download_location
        self.audio_format = audio_format
        self.quality = quality

    def __repr__(self):
        return (f"UserPreferences(download_location={self.download_location}, "
                f"audio_format={self.audio_format}, quality={self.quality})")