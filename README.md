# A Music Discovery App

The following guide will explain how to install and run this app locally on your own machine.

## Clone this repository to your local machine
1. In a linux terminal, clone this repository: `git clone https://github.com/NJIT-CS490-SP21/project1-ya82`
2. Enter your new directory: `cd project1-ya82`

## Create a Spotify API Application
1. Follow the Spotify quickstart instructions to set up your account and register your application: https://developer.spotify.com/documentation/web-api/quick-start/

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