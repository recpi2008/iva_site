from django.shortcuts import render

def index(request):
    # contex = {
    #     'title': 'Andrey Iva - main',
    #     'div_class_social': 'social-media-links',
    #     'class_social':"social-media",
    # }
    return render(request, 'mainapp/index.html')
