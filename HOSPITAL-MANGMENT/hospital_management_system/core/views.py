from django.http import HttpResponse
from django.shortcuts import render

from .models import patient_a

# Create your views here.

def index(requst):
    return HttpResponse("<h1> hospital mangment system website")



def patient_signup(requst):
    First_name=requst.POST.get('firstname')
    print(First_name)
    Last_name=requst.POST.get('lastname')
    Phone_Number1=requst.POST.get('phone')
    Address=requst.POST.get('Address')
    Email_Address=requst.POST.get('email')
    Birth_Date=requst.POST.get('birthday')
    patientֹID= requst.POST.get('patientid')
    password_patientֹ= requst.POST.get('psw')

    mypatientdata=patient_a(patientֹID= patientֹID ,First_name=First_name,Last_name=Last_name,Phone_Number=Phone_Number1,Address=Address,Email_Address=Email_Address,Birth_Date=Birth_Date,password_patientֹ=password_patientֹ)
    mypatientdata.save()
    return render(requst,'patient_signup.html')


def login_Doctor(requst):
    return render(requst,'login_Doctor.html')

def signup_Doctor(requst):
    return render(requst,'signup_Doctor.html')

def login_patient(requst):
    return render(requst,'login_patient.html')

def AdminLogin (requst):
    return render(requst,'AdminLogin.html')

def AskDoctor (requst):
    return render(requst,'AskDoctor.html')    


     