# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:38:02 2018

@author: Evan Wain
Reddit data scraper
"""

import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='O46duMM7Pm0ZXA',
                     client_secret='Ow_w8H5H_80UbNgolGVu7j3tICM',
                     user_agent='Finance Miner',
                     password='Aug151990'
                     )
subreddit = reddit.subreddit('investing')

top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=1000)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)
    
topics_dict = {"title":[], \
               "score":[], \
               "id":[], "url":[], \
               "comms_num":[], \
               "created":[], \
               "body":[]
               }

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
topics_data.to_csv('INVESTING.csv')

