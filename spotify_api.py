import requests
import os
from dotenv import load_dotenv, find_dotenv
import random


def fetch_access_token():
    load_dotenv(find_dotenv())

    # Retrieves access token
    auth_url = 'https://accounts.spotify.com/api/token'

    params = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
        'client_secret': os.getenv('SPOTIFY_CLIENT_SECRET')
    }

    response = requests.post(auth_url, params)
    data = response.json()
    return data['access_token']


access_token = fetch_access_token()


class Spotify:
    """The Spotify API allows access to data about the songs, artists, and albums available on Spotify"""
    def __init__(self):
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

        song_artists = []
        for artist in song['artists']:
            song_artists.append(artist['name'])

        self.Name = song['name']
        self.Artists = song_artists
        self.Image = song['album']['images'][0]['url']
        self.Preview = song['preview_url']
