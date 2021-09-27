import os
import json
from django.shortcuts import render
from songsapp.models import Songs, ContentCategory, Blog

MODULE_DIR = os.path.dirname(__file__)


def songs(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/product.json')
    contex = {
        'title': 'AndreyIva - ТРЕКИ',
        'songs': Songs.objects.all(),
    }
    return render(request, 'songsapp/songs.html', contex)


def about(request):
    contex = {
        'title': 'AndreyIva - ОБО МНЕ',
    }
    return render(request, 'songsapp/about.html', contex)

def blog(request):
    contex = {
        'title': 'AndreyIva - БЛОГ',
        'blogs': Blog.objects.all(),
    }
    return render(request, 'songsapp/blog.html', contex)
