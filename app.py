from flask import Flask, render_template
import os
import api

app = Flask(__name__)


@app.route('/')
def homepage():
    song = api.Song()
    
    if song.Error == True:
        return render_template(
            'error.html'
            )
    else:
        return render_template(
            'index.html',
            song_name=song.Name,
            song_artist=song.Artist,
            song_image=song.Image,
            song_preview=song.Preview,
            song_lyrics=song.Lyrics
        )


app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
