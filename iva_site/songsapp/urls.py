from django.urls import path
from songsapp.views import *

app_name = 'songs'
urlpatterns = [
    path('', songs, name='song'),
    path('about/', about, name='about'),
    path('fotogalery/', fotogalery, name='fotogalery'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),

]

