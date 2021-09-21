import os
import json
from django.shortcuts import render
from songsapp.models import Songs, ContentCategory

MODULE_DIR = os.path.dirname(__file__)



def songs(request):
    file_path = os.path.join(MODULE_DIR,'fixtures/product.json')
    contex = {
        'title': 'Andrey Iva - Songs',
        'songs': Songs.objects.all(),
    }
    return render(request, 'songsapp/songs.html', contex)
