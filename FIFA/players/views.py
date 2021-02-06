import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Players should b here")

def players_view(request, name):
    return render(
        request,
        'players/about.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )