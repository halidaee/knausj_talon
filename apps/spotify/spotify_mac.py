from talon import Module, app
from talon.mac import applescript

# mod = Module()
# apps = mod.apps
# apps.spotify = "app.name: Spotify"
# apps.spotify = """
# os: mac
# and app.bundle: com.spotify.client
# """

mod = Module()
apps = mod.apps

@mod.action_class
class Actions:
    def spotify_pause():
        """Pause Spotify"""
        applescript.run("tell application \"Spotify\" to pause")
    
    def spotify_play():
        """Play Spotify"""
        applescript.run("tell application \"Spotify\" to play")
        
    def spotify_next():
        """Go to next song in Spotify"""
        applescript.run("tell application \"Spotify\" to next track")
        
    def spotify_previous():
        """Go to previous song in Spotify"""
        applescript.run("tell application \"Spotify\" to previous track")