# Using Python lib spotipy 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

user_spotify_credentials = SpotifyClientCredentials(client_id='ABC',client_secret='XYZ')
sp = spotipy.Spotify(client_credentials_manager=user_spotify_credentials)

print(sp)

# End