from django.http import HttpResponse
from django.shortcuts import render
 
# Create your views here.

def index(requst):
    return HttpResponse("<h1> hospital mangment system website")



def patient_signup(requst):
    return render(requst,'patient_signup.html')
