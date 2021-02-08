from django.urls import path
from players import views
from players.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="players/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path('players/<name>', views.player_view, name='player_page'),
    path('contact/', views.contact_view, name='contact_page'),
    path('about/', views.about_view, name='about_page'),
    path('home/', views.home_view, name='home_page'),
    path('log/', views.log_message_view, name='log_page')
]


