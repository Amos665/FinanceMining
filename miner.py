# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:23:21 2018

@author: Amos665
"""

import tweepy, codecs

#app authentications
from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
        )

#let Tweepy set up an instance of the REST API
auth_one = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth_one.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth_one)

#fill in your search query and store your results in a variable
results = api.search(q = "day trading", lang = "en", result_type = "recent", count = 1000)

#use the codecs library to write the text of the Tweets to a .txt file
file = codecs.open("stockinfo.txt", "w", "UTF-8")
for result in results:
    file.write(result.text)
    file.write("\n")
file.close()