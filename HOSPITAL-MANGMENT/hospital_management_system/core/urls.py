from django.urls import path
from .views import *
urlpatterns=[
    path('',index) ,
    path('patient_signup/',patient_signup),
    path('login_Doctor/',login_Doctor),
    path('signup_Doctor/',signup_Doctor),
    path('login_patient/',login_patient,name="login_patient"),
    path('AdminLogin/',AdminLogin,name="AdminLogin"),
    path('AskDoctor/',AskDoctor,name="AskDoctor"),
]

