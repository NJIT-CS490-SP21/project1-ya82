from flask import Flask
import os
import spotify_api


def main():
    app = Flask(__name__)
    
    
    @app.route('/')
    def hello_world():
        song = spotify_api.Spotify()
        return song.Name
        
    app.run(
        port = int(os.getenv('PORT', 8080)),
        debug=True
        )
        
        
main()