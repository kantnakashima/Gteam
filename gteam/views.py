from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def afterlogin(request):
    return render(request, 'afterlogin.html')
