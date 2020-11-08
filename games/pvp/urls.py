from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'pvp'

urlpatterns = [
    path('play', csrf_exempt(Play.as_view()), name='play'),
    path('lounge', csrf_exempt(Lounge.as_view()), name='war_lounge'),
    path('character/create/avatar', csrf_exempt(Create.as_view()), name='create_avatar'),
]