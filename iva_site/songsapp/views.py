import os
import json
from django.shortcuts import render
from songsapp.models import Songs, ContentCategory

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
