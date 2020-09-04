from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'pvp'

urlpatterns = [
    path('', csrf_exempt(Lounge.as_view()), name='lounge'),
    path('create/avatar', csrf_exempt(Create.as_view()), name='create_avatar'),
]