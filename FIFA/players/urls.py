from django.urls import path
from players import views

urlpatterns = [
    path('',views.home,name='home'),
    path('players/<name>', views.player_view, name='player_page'),
    path('contact/', views.contact_view, name='contact_page'),
    path('about/', views.about_view, name='about_page'),
    path('home/', views.home_view, name='home_page'),
]