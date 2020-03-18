# YouTube to Spotify Playlist
A python script that creates a playlist on Spotify made up of songs you liked on Youtube. 
This program goes through your playlist of liked videos on Youtube and records the artist and song name. It sends this data over to your Spotify account and searches for each track and adds it to a newly created playlist of only the songs you liked on Youtube. 

## Procedure
1. Start off by installing the packages in the [install.txt](https://github.com/abhigya-ps/YouTube-to-Spotify/blob/master/install.txt) file. 

2. **Linking your Spotify account:**

     a. Note down your Spotify User ID (your username) available in the link below:
    https://www.spotify.com/us/account/overview/
    
     b. And note down your Oauth Token by clicking "Get Token" in the link below:
    https://developer.spotify.com/console/post-playlists/
    This token gives your script permission to create a playlist on your behalf. Add both User ID and       Oauth Token to the spotify_access.py file.
    
3. **Accessing your Youtube account:**

     a. Enable "YouTube Data API v3" by looking it up in the Google APIs library in the link below:
    https://console.developers.google.com/apis/library/
    
     b. **Creating credentials:** Visit the link below and hit "CREATE CREDENTIALS". 
    https://console.developers.google.com/apis/credentials
    
     First, get your API key. Then, create an Oauth Client ID. Download your Oauth 2.0 Client ID file. Copy all credentials info to the      clientsecret.py file. Your script will now have access to your Youtube account.
   
     *For more info on YouTube Data API, visit here: https://developers.google.com/youtube/v3/getting-started/*
   
4. Finally, run the program. It will ask you to follow a link that will have you log into your google account and provide you with an authorization code to continue with the program. Completion of this step ensures that the script has access to your account. (Regenerate Oauth Tokens if they stop working)

## Notes
Credit goes to TheComeUpCode who posted an instructional video for this program on her Youtube channel. Please watch her video for more details:

https://www.youtube.com/watch?v=7J_qcttfnJA

![playlist image](https://github.com/abhigya-ps/YouTube-to-Spotify/blob/master/images/youtube%20to%20spotifyy.PNG)



 

    

