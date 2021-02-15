import requests
from dotenv import load_dotenv, find_dotenv
import os

def request_song_info(song_title, artist_name):
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

    return response.json()


response = request_song_info('Lone Digger', 'Caravan Palace')
lyrics_url = response['response']['hits'][0]['result']['url']
print(lyrics_url)
