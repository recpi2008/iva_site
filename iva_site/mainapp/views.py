from django.shortcuts import render

def index(request):
    contex = {
        'title': 'Andrey Iva - main',
    }
    return render(request, 'mainapp/index.html',contex)
