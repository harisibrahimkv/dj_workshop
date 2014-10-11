from django.shortcuts import render
from django.http import HttpResponse

from .forms import HashtagForm
from .utils import fetch_tweets, save_tweets

# Create your views here.

def user_input(request):
    if request.method == "GET":
        form = HashtagForm()
    else:
        form = HashtagForm(request.POST)
        if form.is_valid():
            hashtag = form.cleaned_data['hashtag']
            tweets = fetch_tweets(hashtag)
            save_tweets(tweets, hashtag)
            return HttpResponse("Gotcha!")

    return render(request, 'user_input.html', { 'form': form })
            
