from django.http import HttpResponse
from django.shortcuts import render
 
# Create your views here.

def index(requst):
    return HttpResponse("<h1> hospital mangment system website")



def patient_signup(requst):
    return render(requst,'patient_signup.html')


def login_Doctor(requst):
    return render(requst,'login_Doctor.html')

def signup_Doctor(requst):
    return render(requst,'signup_Doctor.html')

def login_patient(requst):
    return render(requst,'login_patient.html')