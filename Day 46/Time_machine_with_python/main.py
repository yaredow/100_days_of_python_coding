from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests
import os
import lxml

user_input = input("what year you would like to travel to in YYY-MM-DD? ")
clientID = "a3cfcc87f11d4eeaa305abfdfc0d5abe"
ClientSecret = "815e68adbba54afa929c45ba2010d77f"

response = requests.get("https://www.billboard.com/charts/hot-100/" + user_input)
billboard_data = response.text
soup = BeautifulSoup(billboard_data, "lxml")
song_names_spans = soup.find_all("h3", id="title-of-a-story")
song_names = [song.getText() for song in song_names_spans]
print(song_names)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=clientID,
        client_secret=ClientSecret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_uris = []
year = user_input.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)