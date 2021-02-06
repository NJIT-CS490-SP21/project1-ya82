from flask import Flask
import os
from spotify_api import fetch_song_data


def main_frontend():
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        song_data = fetch_song_data()
        return song_data['Name']
        
    app.run(
        port = int(os.getenv('PORT', 8080))
        )
        
main_frontend()