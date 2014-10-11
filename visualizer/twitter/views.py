from django.shortcuts import render
from django.http import HttpResponse

from .forms import HashtagForm

import json

# Create your views here.

def user_input(request):
    if request.method == "GET":
        form = HashtagForm()
    else:
        form = HashtagForm(request.POST)
        if form.is_valid():
            hashtag = form.cleaned_data['hashtag']
            return HttpResponse("Gotcha!")

    return render(request, 'user_input.html', { 'form': form })
            
