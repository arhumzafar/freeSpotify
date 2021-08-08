## freeSpotify
#### Arhum Zafar - 2021

 <br>
 I created this program to see if I could detect when an advertisment plays by monitoring the type of track that is currently being played by Spotify.

### Installs
```
git clone https://github.com/arhumzafar/freeSpotify.git
```
```
cd freeSpotify.py
```
```
pip install pynput
```
```
pip install spotipy
``` 
<br>

### How to start

1. Start by heading over to https://developer.spotify.com/dashboard and sign in with your Spotify account.
2. Click on **Create An App** option and provide an app name and description.
3. Go to 'EDIT SETTINGS' and fill in the Redirect URIs placeholder with http://localhost:8080/, and click on Save.
4. Copy the Client ID and Client Secret and paste it in the corresponding place holders in freeSpotify.py.
5. Paste the path to the spotify application on your computer in the PATH placeholder in freeSpotify.py.
6. Paste your spotify username in the username placeholder in freeSpotify.py

### Running 
1. Open Spotify and start a track.
2. Run the script in the background by typing: `python3 freeSpotify.py` in the correct directory.
3. Enjoy your playlist without any ads :)
<br>

<br>

thanks.