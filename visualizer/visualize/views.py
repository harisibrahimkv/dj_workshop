from django.http import HttpResponse
from django.shortcuts import render

import datetime

# Create your views here.

def entity_visualizer(request):
    current_date = datetime.datetime.now()
    var_dictionary = {"date_now": current_date}
    return render(request, "hello_world.html", var_dictionary)
