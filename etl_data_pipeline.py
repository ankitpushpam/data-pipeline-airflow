import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs


def run_twitter_etl():
    # Twitter API access keys and secrets
    access_key = ""
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""

    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)
    auth.set_access_token(consumer_key, consumer_secret)

    # Creating an API object
    api = tweepy.API(auth)

    # Extract tweets
    tweets = api.user_timeline(
        screen_name='@elonmusk',
        count=200,
        include_rts=False,
        tweet_mode='extended'
    )

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            "text": text,
            "favorite_count": tweet.favorite_count,
            "retweet_count": tweet.retweet_count,
            "created_at": tweet.created_at
        }
        tweet_list.append(refined_tweet)

    # Transform to a Pandas DataFrame and save to an S3 bucket
    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://bucket-name/twitter_data.csv")
