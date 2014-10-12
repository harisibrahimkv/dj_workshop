from django.http import HttpResponse
from django.shortcuts import render

from twitter.models import Tweet

import redis
import random
import datetime

from datetime import timedelta

# Create your views here.

def entity_visualizer(request):
    r = redis.StrictRedis()
    the_count = r.get("tweets_count")
    l = r.zrange("popular_tweets", 0,
                 -1, desc=True, withscores=True,
                 score_cast_func=int)
    popular_tweets = []
    for i in l:
        tweet = Tweet.objects.get(id = int(i[0]))
        score = i[1]
        popular_tweets.append((tweet, score))

    ####

    tweet_list = Tweet.objects.all().order_by('created_at')
    number_of_days = 2
    color_set = []
    for i in range(0, number_of_days):
        r = random.randrange(0, 220, 3)
        g = random.randrange(0, 220, 3)
        b = random.randrange(0, 220, 3)
        color_set.append(dict(fillColor = "rgba(%s,%s,%s,0.5)" % (r, g, b),
                              strokeColor = "rgba(%s,%s,%s,1)" % (r, g, b),
                              pointColor = "rgba(%s,%s,%s,1)" % (r, g, b),
                              pointStrokeColor = "#fff"))

    start_date = tweet_list[0].created_at

    data_set_count = 0
    tweet_iter = 0
    for i in range(0, number_of_days):
        tweets_per_hour = []
        for j in range(0, 24):
            cur_date = start_date + timedelta(days=i, hours=j)
            tweet_count = 0
            while tweet_iter < len(tweet_list):
                tweet_datetime = tweet_list[tweet_iter].created_at
                if tweet_datetime >= cur_date and tweet_datetime <= cur_date + timedelta(hours=1):
                    tweet_iter += 1
                    tweet_count += 1
                else:
                    break
            tweets_per_hour.append(tweet_count)
        color_set[i]['data'] = tweets_per_hour
    the_data_set = []
    message = None
    
    for i in range(0, 2):
        the_data_set.append(color_set[i])
   
    the_label_set = [i for i in range(0,24)]

    ####

    current_date = datetime.datetime.now()
    var_dictionary = {
        'date_now': current_date,
        'the_data_set': the_data_set,
        'the_label_set': the_label_set,
        'tweet_count' : the_count,
        'tweet_list': popular_tweets,
    }
    return render(request, "hello_world.html", var_dictionary)
