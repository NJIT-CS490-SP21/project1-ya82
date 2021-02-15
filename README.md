# A Music Discovery App

## Quickstart Guide
The following guide will explain how to configure this music discovery app.

### 1. Clone this repository to your local machine
In a Linux terminal, clone this repository: `git clone https://github.com/NJIT-CS490-SP21/project1-ya82`

### 2. Configure environment variables
There are three needed environment variables. These will need to be configured using Heroku.
* Your Spotify client id: `SPOTIFY_CLIENT_ID`
* Your Spotify client secret: `SPOTIFY_CLIENT_SECRET`
* Your Genius access token: `GENIUS_ACCESS_TOKEN`

### 3. Deploy!
Deploy the app to Heroku. Heroku will install the app requirements, load the environment variables, and deploy the app to the given domain name.


## Potential future features

### Ability to select a genre
A dropdown menu to select a genre could be a useful future.
* The dropdown menu would be implemented into the HTML file. When selected, it could redirect to a url that would display a song of that genre.
* A new Flask function and route would be needed. (Ex: @app.route('/pop'))
* This function would then input the genre into the Spotify class.
* The Spotify class could then use Spotify's "Get Recommendations" endpoint to get a list of popular songs of that genre.
* The class could then select a song at random to be displayed.

### Ability to scroll through different songs
Rather than refreshing the page to view a new song, the user would be able to see the songs displayed in row. The song in the middle would be the currently playing song and display additional information. Clicking on the left or right arrows would switch songs.
* Would require the app to continuously load songs to ensure the row of songs is properly filled.
* An array of songs could be used to keep track of the row. Using the class structure of the api calls, song data could be stored in each element of the array.
* New songs could be called to replace elements in the array as needed. (Ex: The user keeps clicking left to view more songs)
* HTML file would need to be configured to display the row of elements and continuously update with new information.
* CSS file could make this aesthetically pleasing with a clean swiping animation as the user cycles through the list of songs. CSS has support for keyframes and animation.

## Technical issues encountered
* One technical issue that was encountered was fetching the access token from Spotify. Previously, a Spotify access token was requested only at program startup. However, Spotify access tokens are only valid for one hour. To remedy this, the app now requests a new access token when a user visits the page.
* Another technical issue encountered was choosing a random artist from the artist_id dictionary. My original solution was to have a separate list with the artist names and to generate a random number index, thus choosing the random artist to select. After some research I discovered a much better solution, the method random.choice() chooses a random element from a list. Thus, `artist = random.choice(list(artist_ids))` proved to be a much cleaner solution the problem.
* A third technical issue encountered was the best way for app.py to grab the song data from api.py. Initially, I had a function in api.py gather the information and return an array with the data. However, I realized that a cleaner approach would be to implement a class instead and have the data be elements of the class. This is a cleaner solution for extra headroom for additional features that could be added in the future, such as loading or displaying multiple songs at once.
