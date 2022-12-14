from django.urls import path
from .views import *
urlpatterns=[
    
    path('',index) ,
    path('patient_signup/',patient_signup),
    ]
