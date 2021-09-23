from django.urls import path
from songsapp.views import *

app_name = 'songs'
urlpatterns = [
    path('', songs, name='song'),
    path('about/', about, name='about'),
]
