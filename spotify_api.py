import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

load_dotenv(find_dotenv())

def get_access_token(): # Retrieves access token
    BASE_URL = 'https://accounts.spotify.com/api/token'
    
    params = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
        'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET')
    }
    
    response = requests.post(BASE_URL, params)
    data = response.json()
    return data['access_token']
    
    
def fetch_song_data(): # Restructure into a class
    
    artist_ids = {
        'Caravan Palace': '37J1PlAkhRK7yrZUtqaUpQ',
        'Of Monsters and Men': '4dwdTW1Lfiq0cM8nBAqIIz',
        'SIAMES': '68NOjWuVYBRXzYwhel3jAl'
    }
    
    artist = random.choice(list(artist_ids))
    
    BASE_URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(
        id=artist_ids[artist]
        )
    
    header = {
        'Authorization': 'Bearer {token}'.format(token=get_access_token())
    }
    
    params = {
        'market': 'US'
    }
    
    
    response = requests.get(
        BASE_URL,
        headers=header,
        params=params
        )
        
    data = response.json()
    tracks = data['tracks']
    song = random.choice(tracks)

    song_artists = []
    for artist in song['artists']:
        song_artists.append(artist['name'])
    
    song_data = {
        'Name': song['name'],
        'Artists': song_artists,
        'Image': song['album']['images'][0]['url'],
        'Preview': song['preview_url']
    }
    
    return song_data
