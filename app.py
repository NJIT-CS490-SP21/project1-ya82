from flask import Flask, render_template
import os
import spotify_api

app = Flask(__name__)


@app.route('/')
def homepage():
    song = spotify_api.Spotify()
    return render_template(
        'index.html',
        song_name=song.Name,
        song_artists=song.Artists,
        len_artists=len(song.Artists),
        song_image=song.Image,
        song_preview=song.Preview
    )


app.run(
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
