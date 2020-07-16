import lyricsgenius
import tweepy
import random
import os
from os import environ

CONSUMER_API_KEY = environ['CONSUMER_API_KEY']
CONSUMER_API_SECRET_KEY = environ['CONSUMER_API_SECRET_KEY']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET_TOKEN = environ['ACCESS_SECRET_TOKEN']
GENIUS_CLIENT_ACCESS_TOKEN = environ['GENIUS_CLIENT_ACCESS_TOKEN']

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

all_songs = ["Yesterday", "Pretender", "I LOVE...", "パラボラ Parabola", "宿命 (Shukumei)", "ビンテージ (Vintage)", "Stand By You", "Saigo no Koiwazurai", "Travelers", "Last Song", "Laughter", "Rowan", "Fire Ground", "Amazing", "バッドフォーミー (Bad for Me)"]
            
def get_raw_lyrics():
    genius = lyricsgenius.Genius(GENIUS_CLIENT_ACCESS_TOKEN)
    random_song_title = random.choice(all_songs)
    lyrics = genius.search_song(random_song_title, "Official HIGE DANdism").lyrics
    song = random_song_title
    return lyrics, song

def get_tweet_from(lyrics):
    lines = lyrics.split('\n')
    for index in range (len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines) - 1)
    tweet = lines[random_num] + "\n" + lines[random_num + 1]
    tweet = tweet.replace("\\", "")
    return tweet

lyrics, song = get_raw_lyrics()
tweet = get_tweet_from(lyrics)
status = api.update_status(tweet)
bio = api.update_profile(description=song)

























































