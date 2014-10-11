import json
import datetime
# from twython import Twython

from .models import Tweet

def fetch_tweets(hashtag):
    # twitter = Twython(
    #     settings.TWITTER_CONSUMER_KEY,
    #     settings.TWITTER_CONSUMER_SECRET,
    #     settings.OAUTH_TOKEN,
    #     settings.OAUTH_TOKEN_SECRET,
    # )
    # tweets = twitter.search(
    #     q = h,
    #     count = 100,
    # )
    f = open("/home/haris/dj_workshop/visualizer/twitter/new_tweets.txt", "r")
    tweets = json.loads(f.read())
    return tweets

def save_tweets(tweets, hashtag):
    for tweet in tweets:
        author = tweet['user']['screen_name']
        created_at = datetime.datetime.strptime(
            tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'
        )
        text = tweet['text']
        tweet, created = Tweet.objects.get_or_create(
            hashtag = hashtag,
            author = author,
            created_at = created_at,
            text = text
        )
