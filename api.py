import requests
import os
from dotenv import load_dotenv, find_dotenv
import random

# Double check how long access token is valid for
def fetch_spotify_access_token():
    load_dotenv(find_dotenv())

    auth_url = 'https://accounts.spotify.com/api/token'

    params = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
        'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET')
    }

    response = requests.post(auth_url, params)
    data = response.json()
    return data['access_token']


def fetch_lyrics_url(song_title, artist_name):
    load_dotenv(find_dotenv())
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + os.getenv('GENIUS_ACCESS_TOKEN')}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(
        search_url,
        data=data,
        headers=headers
        )

    data = response.json()
    lyrics_url = data['response']['hits'][0]['result']['url']
    
    return lyrics_url


access_token = fetch_spotify_access_token()


class Song:
    """The Spotify and Genius API allows access to data about songs, artists, and albums"""
    def __init__(self):
        try:
            self.Error = 'temp'
            while self.Error != False:
                artist_ids = {
                    'Caravan Palace': '37J1PlAkhRK7yrZUtqaUpQ',
                    'Of Monsters and Men': '4dwdTW1Lfiq0cM8nBAqIIz',
                    'SIAMES': '68NOjWuVYBRXzYwhel3jAl'
                }
        
                artist = random.choice(list(artist_ids))
        
                base_url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(
                    id=artist_ids[artist]
                )
        
                header = {
                    'Authorization': 'Bearer {token}'.format(token=access_token)
                }
        
                params = {
                    'market': 'US'
                }
        
                response = requests.get(
                    base_url,
                    headers=header,
                    params=params
                )
        
                data = response.json()
                tracks = data['tracks']
                song = random.choice(tracks)
    
                self.Name = song['name']
                self.Artist = song['artists'][0]['name']
                self.Image = song['album']['images'][0]['url']
                self.Preview = song['preview_url']
                self.Lyrics = fetch_lyrics_url(self.Name, self.Artist)
                
                song_attributes = [self.Name, self.Artist, self.Image, self.Preview, self.Lyrics]
                self.Error = False
                for attribute in song_attributes:
                    if attribute == None:
                        self.Error = True
        except:
            self.Error = True
