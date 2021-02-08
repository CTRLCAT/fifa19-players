import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from players.forms import LogMessageForm
from players.models import LogMessage
from django.views.generic import ListView

# Create your views here.
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

# def home(request):
#     return HttpResponse("Hello, Django!")

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

def log_message_view(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "players/log_message.html", {"form": form})