from twython import Twython

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
    print type(tweets)
    print type(tweets[0])
