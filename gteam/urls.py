from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("userlogin", views.userlogin, name="userlogin"),
    path("mainmenu", views.mainmenu, name="mainmenu"),
    path("usersignup", views.usersignup, name="usersignup"),
    path("reservationchange", views.reservationchange, name="reservationchange"),
    path("reservationcompleted", views.reservationcompleted, name="reservationcompleted"),
    path("userreservationdetails", views.userreservationdetails, name="userreservationdetails"),
    path("userreservationlistscreen", views.userreservationlistscreen, name="userreservationlistscreen"),
]