# A Music Discovery App

The following guide will explain how to install and run this app locally on your own machine.

## Clone this repository to your local machine
1. In a Linux terminal, clone this repository: `git clone https://github.com/NJIT-CS490-SP21/project1-ya82`
2. Enter your new directory: `cd project1-ya82`

## Create a Spotify API Application
1. Follow the Spotify quick start instructions to set up your account and register your application: https://developer.spotify.com/documentation/web-api/quick-start/

## Installation requirements
Install the project's requirements.
1. `pip install Flask`
2. `pip install requests`
3. `pip install python-dotenv`

## Configure your .env file
1. Create a .env file in the project directory: `touch .env`
2. Copy your Client ID and Client Secret from your Spotify API Application: https://developer.spotify.com/dashboard/applications
3. Paste them into the .env file with the following format


`export SPOTIFY_CLIENT_ID='PASTE_CLIENT_ID_HERE'`


`export SPOTIFY_CLIENT_SECRET='PASTE_CLIENT_SECRET_HERE'`

## Run!
1. Run the application with: `python app.py`
2. Visit http://127.0.0.1:8080/ in your web browser to preview the application.

# Known problems

1. Spotify preview is not available for all songs

Potential Solution: Only display songs that have a valid preview available

# Potential future features

## Ability to select a genre

A dropdown menu to select a genre could be a useful future.
* The dropdown menu would be implemented into the HTML file. When selected, it could redirect to a url that would display a song of that genre.
* A new Flask function and route would be needed. (Ex: @app.route('/pop'))
* This function would then input the genre into the Spotify class.
* The Spotify class could then use Spotify's "Get Recommendations" endpoint to get a list of popular songs of that genre.
* The class could then select a song at random to be displayed.


# Technical issues encountered

1. One technical issue that was encountered was fetching the access token from Spotify. Initially, a new access key was requested every time a user refreshed a page. Realizing this was inefficient, I placed the fetch_access_code() function outside of the class definition and verified that the function ran only once - at program execution time.
2. Another technical issue encountered was choosing a random artist from the artist_id dictionary. My original solution was to have a separate list with the artist names and to generate a random number index, thus choosing the random artist to select. After some research I discovered a much better solution, the method random.choice() chooses a random element from a list. Thus, `artist = random.choice(list(artist_ids))` proved to be a much cleaner solution the problem.
3. A third technical issue encountered was the best way for app.py to grab the song data from spotify_api.py. Initially, I had a function in spotify_api gather the information and return an array with the data. However, I realized that a cleaner approach would be to implement a class instead and have the data be elements of the class.
