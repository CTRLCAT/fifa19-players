import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Players should b here")

def player_view(request, name):
    return render(
        request,
        'players/player.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def contact_view(request):
    return render(request, 'players/contact.html')

def home_view(request):
    return render(request, 'players/home.html')

def about_view(request):
    return render(request, 'players/about.html')