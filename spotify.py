# Using Python lib spotipy
import spotipy
import Credentials as cr 
from spotipy.oauth2 import SpotifyClientCredentials

# Using credentials to access Spotify Web API  
user_spotify_credentials = SpotifyClientCredentials(client_id=cr.my_client_id,client_secret=cr.my_client_secret)

# Spotify object 
sp = spotipy.Spotify(client_credentials_manager=user_spotify_credentials)

# Extract the playlist id
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"
playlist_uri = playlist_link.split('/')[4]

# data about albums, artists and tracks  
data = sp.playlist_tracks(playlist_id=playlist_uri) 


#print(data)

# album list will be used to store dictionaries 
# representing list of individual albums
album_list = []

for row in data['items']:
    for key, value in row.items():
        if(key == 'track'):
            album_id = value['album']['id']     
            album_name = value['album']['name']         
            album_release_date = value['album']['release_date']     
            album_total_tracks = value['album']['total_tracks']     
            album_url = value['album']['external_urls']['spotify']
            album_dict = {'album_id': album_id , 'album_name': album_name, 'album_release_date': album_release_date, 
                          'album_total_tracks' : album_total_tracks, 'album_url' : album_url}  
            album_list.append(album_dict)

# artist list will be used to store dictionaries 
# representing list of individual artists
artist_list = [] 
for row in data['items']:
    for key, value in row.items():
        if(key == 'track'):
            for artist in value['artists']: 
                print(artist['name'])
