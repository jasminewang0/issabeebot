#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '9Gh6P0tYP12fe9oRw2jd44S9m'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'kIHwBge5Mo1T4EePaIkT0JcIQcxLRvQqGxjTuNb28oHW4cNj06'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '920124656853581826-ccy0j3Q8f11d6DYs6HjdrawzzegaHiq'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'hCbeJPWJuyAnw7IaFYV1xcPBu1r0O6oyCxms1qhTNf9wZ'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(10)#Tweet every 15 minutes
