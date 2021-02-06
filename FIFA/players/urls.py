from django.urls import path
from players import views

urlpatterns = [
    path('',views.home,name='home'),
    path('players/<name>', views.players_view, name='los_players'),
]