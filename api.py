import requests
import os
import random

artist_ids = {
                'Caravan Palace': '37J1PlAkhRK7yrZUtqaUpQ',
                'Of Monsters and Men': '4dwdTW1Lfiq0cM8nBAqIIz',
                'SIAMES': '68NOjWuVYBRXzYwhel3jAl'
            }


def fetch_spotify_access_token():
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


def fetch_song_data(artist):
    base_url = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_ids[artist])
    header = {'Authorization': 'Bearer {token}'.format(token=fetch_spotify_access_token())}
    params = {'market': 'US'}
    response = requests.get(
        base_url,
        headers=header,
        params=params
    )
    data = response.json()
    tracks = data['tracks']
    song_data = random.choice(tracks)
    return song_data


class Song:
    """The Spotify and Genius API allow access to data about songs, artists, and albums"""

    def __init__(self):
        counter = 0
        self.Error = True
        while self.Error is True and counter < 25:
            counter += 1
            self.Error = False
            
            artist = random.choice(list(artist_ids))
            song_data = fetch_song_data(artist)

            self.Name = song_data['name']
            self.Artist = song_data['artists'][0]['name']
            self.Image = song_data['album']['images'][0]['url']
            self.Preview = song_data['preview_url']
            self.Lyrics = fetch_lyrics_url(self.Name, self.Artist)

            song_attributes = [self.Name, self.Artist, self.Image, self.Preview, self.Lyrics]
            for attribute in song_attributes:
                if attribute is None:
                    self.Error = True
