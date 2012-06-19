#!/usr/bin/env python

import sys
import tweepy

CONSUMER_KEY = 'consumerkey'
CONSUMER_SECRET = 'consumersecret'
ACCESS_KEY = 'accesskey'
ACCESS_SECRET = 'accesssecret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
api.update_status(sys.argv[1])
