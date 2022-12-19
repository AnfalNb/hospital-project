from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index') ,
    path('patient_signup/',patient_signup),
    # path('login_Doctor/',login_Doctor),
    # path('signup_Doctor/',signup_Doctor),
    # path('login_patient/',login_patient,name="login_patient"),
    # path('AdminLogin/',AdminLogin,name="AdminLogin"),
    # path('AskDoctor/',AskDoctor,name="AskDoctor"),

    path('signup_patient/',signup_patient,name="signup_patient"),
    path('Doctor_signup/',Doctor_signup,name="Doctor_signup"),
    path('login_patient/',login_patient,name="login_patient"),
    path('patient_homepag/',patient_homepage,name="patient_homepage"),
    path('login_Doctor/',login_Doctor,name="login_Doctor"),
    path('AdminLogin/',AdminLogin,name="AdminLogin"),

]







