import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import requests
import youtube_dl

def get_youtube_client():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    scopes = ["https://www.googleapis.com/auth/youtube"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    
    youtube_client = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    return youtube_client

def get_liked_videos(yt_client):
    request = yt_client.videos().list(
        part = "snippet,contentDetails,statistics",
        myRating = "like",
        maxResults = 50
    )
    response = request.execute()

    songs = {}

    for item in response["items"]:
        video_title = item["snippet"]["title"]
        youtube_url = "https://www.youtube.com/watch?v={}".format(
            item["id"])
        
        video = youtube_dl.YoutubeDL({}).extract_info(
            youtube_url, download=False)
        song_name = video["track"]
        artist = video["artist"]

        if song_name is not None and artist is not None:
            songs[song_name] = artist
    
    return(songs)
    

your_client = get_youtube_client()
list_of_songs = get_liked_videos(your_client)
print(list_of_songs)