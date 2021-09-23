from django.shortcuts import render

def index(request):
    contex = {
        'title': 'AndreyIva - Главная',
    }
    return render(request, 'mainapp/index.html',contex)
