import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv()) # This is to load your API keys from .env

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
    
    
def main_backend():
    BASE_URL = 'https://api.spotify.com/v1/browse/new-releases'
    
    header = {
        'Authorization': 'Bearer {token}'.format(token=get_access_token())
    }
    
    params = {
        'country': 'US',
        'limit': 10
    }
    
    response = requests.get(
        BASE_URL,
        headers=header,
        params=params
        )
        
    data = response.json()
    album_names = []
    for album in data['albums']['items']:
        album_names.append(album['name'])
        
    return album_names
    