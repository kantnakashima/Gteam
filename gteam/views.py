from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def mainmenu(request):
    return render(request, 'mainmenu.html')

def usersignup(request):
    return render(request, 'usersignup.html')