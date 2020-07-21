import tweepy
import random
import os
from os import environ

CONSUMER_API_KEY = environ['CONSUMER_API_KEY']
CONSUMER_API_SECRET_KEY = environ['CONSUMER_API_SECRET_KEY']
ACCESS_TOKEN = environ['ACCESS_TOKEN']
ACCESS_SECRET_TOKEN = environ['ACCESS_SECRET_TOKEN']


auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)

file = open('HigedanLyrics.txt', 'r', encoding = 'utf8')
read_file = file.read()
lines = read_file.split('\n\n\n')
random.shuffle(lines)
status = api.update_status(random.choice(lines))
























































