from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def mainmenu(request):
    return render(request, 'mainmenu.html')

def usersignup(request):
    return render(request, 'usersignup.html')

def reservationchange(request):
    return render(request, 'reservationchange.html')

def reservationcompleted(request):
    return render(request, 'reservationcompleted.html')

def userreservationdetails(request):
    return render(request, 'userreservationdetails.html')

def userreservationlistscreen(request):
    return render(request, 'userreservationlistscreen.html')