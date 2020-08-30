from django.urls import path
from .views import *

app_name = 'room'

urlpatterns = [
    path('', Lounge.as_view(), name='lounge'),
]