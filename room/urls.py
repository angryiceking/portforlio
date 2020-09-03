from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'room'

urlpatterns = [
    path('', csrf_exempt(Lounge.as_view()), name='lounge'),
]