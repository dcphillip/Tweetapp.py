#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import sys
import tweepy
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


results = api.search(q="monkey OR coconut", rpp=100, lang="en")

for result in results:
	print result.text.encode('utf-8')
