from django.shortcuts import render

def index(request):
    contex = {
        'title': 'Andrey Iva - Main',
    }
    return render(request, 'mainapp/index.html',contex)
