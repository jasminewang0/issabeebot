#!/usr/bin/env python
import tweepy, time
#from our keys module (keys.py), import the keys dictionary
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twt = api.search(q="love bees")

#list of specific strings we want to check for in Tweets
t = ['love bees']

for s in twt:
    for i in t:
        if i in s.text:
            print s.text
            sn = s.user.screen_name
            m = "@%s YA LIKE JAZZ?" % (sn)
            #s = api.update_status(m, s.id)
            #time.sleep(10)
