# # # # # # # # # # # # # # # # # # # #
# This is the Transformation/Load Layer
# # # # # # # # # # # # # # # # # # # #

import json
import boto3
import pandas as pd
from datetime import datetime
from io import StringIO

def lambda_handler(event, context): 
    s3 = boto3.client('s3')
    Bucket = 'aws-spotify-etl-majid'
    Key = 'raw_data/to_be_processed/'
    
    spotify_data = []
    spotify_keys = []
    
    for file in ((s3.list_objects(Bucket=Bucket, Prefix=Key))['Contents']):
        file_key = file['Key']
        if(file_key.split('.')[-1] == 'json'):
            response = s3.get_object(Bucket = Bucket, Key = file_key) 
            content = response['Body']
            jsonObject = json.loads(content.read())
            spotify_data.append(jsonObject)
            spotify_keys.append(file_key)
            
    for data in spotify_data:
        album_list = album(data)
        artist_list = artist(data)
        songs_list = songs(data) 
        
        album_df = pd.DataFrame.from_dict(album_list)
        album_df = album_df.drop_duplicates(subset=['album_id']) 
        
        artist_df = pd.DataFrame.from_dict(artist_list)
        artist_df = artist_df.drop_duplicates(subset=['artist_id']) 
        
        songs_df = pd.DataFrame.from_dict(songs_list)
        songs_df = songs_df.drop_duplicates(subset=['song_id']) 
        
        album_df['album_release_date'] = pd.to_datetime(album_df['album_release_date'])
        songs_df['song_added'] = pd.to_datetime(songs_df['song_added'])
        
        # Store transformed album, artists and songs data to s3 locations  
        album_key = "transformed_data/album_data/album_transformed_" + str(datetime.now()) + ".csv"
        album_buffer=StringIO()
        album_df.to_csv(album_buffer, index=False)
        album_content = album_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=album_key, Body=album_content)
        
        
        artist_key = "transformed_data/artist_data/artist_transformed_" + str(datetime.now()) + ".csv"
        artist_buffer=StringIO()
        artist_df.to_csv(artist_buffer, index=False)
        artist_content = artist_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=artist_key, Body=artist_content)
        
        song_key = "transformed_data/songs_data/songs_transformed_" + str(datetime.now()) + ".csv"
        song_buffer=StringIO()
        songs_df.to_csv(song_buffer, index=False)
        song_content = song_buffer.getvalue()
        s3.put_object(Bucket=Bucket, Key=song_key, Body=song_content)
        
    s3_resource = boto3.resource('s3')
    for key in spotify_keys:
        copy_source = {
            'Bucket': Bucket,
            'Key' : key 
            
        }
        s3_resource.meta.client.copy(copy_source, Bucket, 'raw_data/already_processed/' + key.split('/')[-1])
        s3_resource.Object(Bucket,key).delete()
             

# album list will be used to store dictionaries 
# representing list of individual albums    
def album(data):
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
    return album_list

# artist list will be used to store dictionaries 
# representing list of individual artists    
def artist(data):

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
    return artist_list 

# songs list will be used to store dictionaries 
# representing list of songs
def songs(data):
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
    return songs_list