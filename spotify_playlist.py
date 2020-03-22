import json
import os

import requests

from exceptions import ResponseException
from spotify_credentials import spotify_token, spotify_user_id
from youtube_playlist import list_of_songs

def create_playlist():
    request_body = json.dumps({
            "name": "Favorites from YouTube",
            "description": "All Liked Youtube Videos",
            "public": True
        })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id)
    response = requests.post(
            query,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(spotify_token)
            }
        )
    response_json = response.json()

    return response_json["id"]

def get_spotify_uri(song_name, artist):
    query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
        song_name,
        artist
    )
    response = requests.get(
        query,
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()
    songs = response_json["tracks"]["items"]

    uri = songs[0]["uri"]

    return uri

def add_song_to_playlist(playlist_id, uris):

    request_data = json.dumps(uris)

    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(
        playlist_id)

    response = requests.post(
        query,
        data=request_data,
            headers={
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )

    if response.status_code != 200:
        raise ResponseException(response.status_code)

    response_json = response.json()
    return response_json

playlist_url = create_playlist()

spotify_url_final = []

for x in list_of_songs:
    spotify_url = get_spotify_uri(x, list_of_songs[x])
    spotify_url_final.append(spotify_url)

add_song_to_playlist(playlist_url, spotify_url_final)

