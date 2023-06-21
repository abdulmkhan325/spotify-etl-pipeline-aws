# Using Python lib spotipy 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

user_spotify_credentials = SpotifyClientCredentials(client_id='84fd22c3658a41e4b72a03597f13b388',client_secret='1b9f47969dec4627a0a1f08ebb6eced4')
sp = spotipy.Spotify(client_credentials_manager=user_spotify_credentials)

print(sp.user(user='22knxy7shmeqilqxlktxwwldq'))

# End