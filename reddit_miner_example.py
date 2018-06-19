# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:38:02 2018

@author: Amos665
Reddit data scraper
"""

import praw
import pandas as pd
import datetime as dt

#authentication credentials
reddit = praw.Reddit(client_id='INSERT YOUR 14 DIGIT APP ID',
                     client_secret='INSERT YOUR CLIENT SECRET',
                     user_agent='INSERT YOUR APP NAME',
                     password='INSERT YOUR PASSWORD'
                     )

#choose your subreddit to scrape
subreddit = reddit.subreddit('your subreddit of choice')

#choose the top posts. Can also sort by .new .hot and .controversial
top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=1000)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)

#creating dictionaries of posts 
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

#formatting the date column correctly
def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
topics_data.to_csv('csv_filename.csv')

