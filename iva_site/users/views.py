from django.shortcuts import render

def login(request):
    contex = {
        'title':'Andrey Iva - Login'
    }
    return render(request, 'users/login.html', contex)

def registration(request):
    contex = {
        'title':'Andrey Iva - Registration'
    }
    return render(request, 'users/registration.html', contex)
