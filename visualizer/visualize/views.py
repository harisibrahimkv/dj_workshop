from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def entity_visualizer(request):
    return render(request, "hello_world.html")
