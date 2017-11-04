#!/usr/bin/env python
import tweepy, time
#from our keys module (keys.py), import the keys dictionary
from keys import keys
from tweepy import *

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twt = api.search(q="love bees", count=100)

#list of specific strings we want to check for in Tweets
t = ['love bees']
count = 0

for s in twt:
    count = count + 1
    print count
    for i in t:
        if i in s.text:
            print s.text
            sn = s.user.screen_name
            m = "@%s YA LIKE JAZZ?" % (sn)
            try:
                s = api.update_status(m, s.id)
                time.sleep(120) #wait 2 mins
            except TweepError:
                print("Already been tweeted, skip this!")
