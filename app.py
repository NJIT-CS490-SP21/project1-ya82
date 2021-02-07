from flask import Flask
import os
import spotify_api


def main():
    app = Flask(__name__)
    
    song = spotify_api.Spotify()
    
    @app.route('/')
    def hello_world():
        return song.Name
        
    app.run(
        port = int(os.getenv('PORT', 8080)),
        debug=True
        )
        
        
main()