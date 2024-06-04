# My Playlist Crafter Bot

This Python project automates the creation of Spotify playlists based on the Billboard Hot 100 chart for a specified date. It utilizes the `requests` library to scrape song titles from the Billboard website and the `spotipy` library to interact with the Spotify API.

## Features
- **Spotify Authentication**: Securely authenticates with Spotify using OAuth.
- **Billboard Chart Scraping**: Retrieves the top 100 songs from a user-specified date on the Billboard Hot 100 chart.
- **Spotify Playlist Creation**: Generates a private Spotify playlist titled with the chosen year.
- **Song Search and Addition**: Searches for each song on Spotify and adds available tracks to the playlist.

## How It Works
1. The user inputs a date in the format `YYYY-MM-DD`.
2. The script scrapes the Billboard Hot 100 chart for the top songs of that week.
3. It then searches for these songs on Spotify and compiles a list of track URIs.
4. A new Spotify playlist is created, and the songs are added to it.

## Setup
To run this project, you'll need to set up Spotify Developer credentials and install the required Python libraries listed in `requirements.txt`.

## Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repo and submit a pull request.
