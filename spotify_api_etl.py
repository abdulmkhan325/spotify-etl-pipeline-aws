# # # # # # # # # # # # # # # #
# This is the Extraction Layer
# # # # # # # # # # # # # # # #
 
import json
import os
import boto3
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime 

def lambda_handler(event, context):
    my_client_id = os.environ.get('client_id')
    my_client_secret = os.environ.get('client_secret')
    
    # Using credentials to access Spotify Web API  
    user_spotify_credentials = SpotifyClientCredentials(client_id=my_client_id,client_secret=my_client_secret)

    # Spotify object 
    sp = spotipy.Spotify(client_credentials_manager=user_spotify_credentials)

    # Extract the playlist id (Global Top 50)
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF"
    playlist_uri = playlist_link.split('/')[4]

    # data about albums, artists and tracks  
    spotify_data = sp.playlist_tracks(playlist_id=playlist_uri) 
    
    # file name 
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    client = boto3.client('s3')
    client.put_object(
        Bucket="aws-spotify-etl-majid",
        Key="raw_data/to_be_processed/" + filename,
        Body=json.dumps(spotify_data)
    )