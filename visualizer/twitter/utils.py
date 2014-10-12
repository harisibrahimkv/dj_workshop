import json
import redis
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

def archive_tweets(tweets, hashtag):
    rq = redis.StrictRedis()
    rq.delete("tweets_count", "popular_tweets")
    for tweet in tweets:
        save_tweet(tweet, hashtag)
        rq.incr("tweets_count", amount = 1)

def save_tweet(tweet, hashtag):
    author = tweet['user']['screen_name']
    created_at = datetime.datetime.strptime(
        tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y'
        )
    text = tweet['text']
    t, created = Tweet.objects.get_or_create(
        hashtag = hashtag,
        author = author,
        created_at = created_at,
        text = text
    )
    if created:
        if 'retweeted_status' in tweet:
            tw = save_tweet(tweet['retweeted_status'], hashtag)
            score_entity(tw.id, tweet['retweeted_status']['retweet_count'])

    return t

def score_entity(id, rt_count):
    rq = redis.StrictRedis(host='localhost', port=6379, db=0)
    rq.zadd("popular_tweets", rt_count, id)
