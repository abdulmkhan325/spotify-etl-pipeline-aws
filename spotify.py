# Using Python lib spotipy
import Credentials as cr
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

user_spotify_credentials = SpotifyClientCredentials(client_id=cr.my_client_id,client_secret=cr.my_client_secret)

sp = spotipy.Spotify(client_credentials_manager=user_spotify_credentials)

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"
playlist_uri = playlist_link.split('/')[4]


print(sp.playlist_tracks(playlist_id=playlist_uri))