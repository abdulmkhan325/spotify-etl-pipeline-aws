# Using Python lib spotipy
import spotipy
import Credentials as cr 
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

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
                artist_id = artist['id']
                artist_name = artist['name']
                artist_url = artist['href']
                artist_dict = {'artist_id': artist_id , 'artist_name': artist_name, 'artist_url': artist_url}  
                artist_list.append(artist_dict)

# songs list will be used to store dictionaries 
# representing list of songs
songs_list = [] 
for row in data['items']:
    song_id = row['track']['id']
    song_name = row['track']['name']
    song_duration = row['track']['duration_ms']
    song_url = row['track']['external_urls']['spotify']
    song_popularity = row['track']['popularity']
    song_added = row['added_at']
    album_id = row['track']['album']['id']
    artist_id = row['track']['album']['artists'][0]['id']
    songs_dict = {'song_id': song_id , 'song_name': song_name, 'song_duration': song_duration,
                  'song_url': song_url , 'song_popularity': song_popularity, 'song_added': song_added,
                  'album_id': album_id , 'artist_id': artist_id}  
    songs_list.append(songs_dict)


album_df = pd.DataFrame.from_dict(album_list)
album_df = album_df.drop_duplicates(subset=['album_id']) 
album_df['album_release_date'] = pd.to_datetime(album_df['album_release_date'])


artist_df = pd.DataFrame.from_dict(artist_list)
artist_df = artist_df.drop_duplicates(subset=['artist_id'])  


songs_df = pd.DataFrame.from_dict(songs_list)
songs_df = songs_df.drop_duplicates(subset=['song_id']) 
songs_df['song_added'] = pd.to_datetime(songs_df['song_added'])

print(songs_df.info())