#### Arhum Zafar
#### July 2021

import os
import time
import pynput
from pynput.keyboard import Key, Controller
import spotipy
from spotipy import util



def closeApp():
    os.system("taskkill /f /im spotify.exe")


def openApp():
    os.statefile(path)


def playSpotify():
    keyboard = Controller()
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)


def lastWindow():
    keyboard = Controller()
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)


def restartSpotify():
    closeApp()
    openApp()
    time.sleep(5)
    playSpotify()
    lastWindow()


def startSpotifyObject(username, scope, clientID, clientSecret, redirectURI):
    token - util.prompt_for_user_token(username, scope, clientID, clientSecret, redirectURI)
    return spotipy.Spotify(auth=token)

def main(username, scope, clientID, clientSecret, redirectURI):
    spotify = setupSpotifyObject(username, scope, clientID, clientSecret, redirectURI)
    current_track = spotify.current_user_playing_track()
            
        try:
            if current_track['currently_playing_type'] == 'ad':
                restartSpotify(path)
                print('Ad skipped')
        except TypeError:
            pass
        
        time.sleep(1)


    if __name__ == '__main__':
        PATH = ''
        spotifyUsername = ""
        spotifyClientID = ""
        spotifyClientSecret = ""
        spotifyAccessScope = "user-read-currently-playing"
        spotifyRedirectURI = "http://localhost:8080/"

        main(spotifyUsername, spotifyAccessScope, spotifyClientID, spotifyClientSecret, spotifyRedirectURI, PATH)
