import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = os.environ.get("Spotify_CLIENT_ID")
CLIENT_SECRET = os.environ.get("Spotify_CLIENT_SECRET")
SPOTIFY_URI = os.environ.get("Spotify_URI")

# ------------- Authentication on Spotify ---------------------
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_URI,
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               username="Oscar Romero"))
# ------ Url for billboard charts website ---------------------
URL = "https://www.billboard.com/charts/hot-100/2023-09-03/"

# ------------ HTML ----------------------------------
response = requests.get(url=URL)
response.raise_for_status()

website_html = response.text

# -----------------  Scrap ------------------------------
soup = BeautifulSoup(website_html, "html.parser")

# Get the top 100 songs
songs = soup.select("li.o-chart-results-list__item h3")

# Songs titles
songs_titles = [song.text.strip() for song in songs]

# ---------------- User input --------------------------
date = input("Which year do you want to travel to? Enter the date in this format YYYY-MM-DD include the '-': ")
year = date.split("-")[0]

# ---------------- Find Songs on Spotify -----------------------------
user_id = sp.current_user()["id"]
songs_uri = []

for song in songs_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uri.append(uri)
    except IndexError:
        print(f"The {song} doesn't exit in Spotify. Skipped.")

# ---------------- Create playlist ------------------------------------
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)
playlist_id = playlist["id"]

# ---------------- Add Songs -------------------------------------
sp.playlist_add_items(playlist_id=playlist_id, items=songs_uri)
