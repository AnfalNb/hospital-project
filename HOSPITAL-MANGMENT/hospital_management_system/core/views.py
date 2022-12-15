from django.http import HttpResponse
from django.shortcuts import render
from .models import patient_a,doctor_a
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate 
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as LL
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import patientform

# Create your views here.

def index(requst):
    return HttpResponse("<h1> hospital mangment system website")

def signup_patient(request):
    form=patientform(request.POST or None)
    if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'signup_patient.html',context)












# def patient_signup(requst):
#     First_name=requst.POST.get('firstname')
#     print(First_name)
#     Last_name=requst.POST.get('lastname')
#     Phone_Number1=requst.POST.get('phone')
#     Address=requst.POST.get('Address')
#     Email_Address=requst.POST.get('email')
#     Birth_Date=requst.POST.get('birthday')
#     patientֹID= requst.POST.get('patientid')
#     password_patientֹ= requst.POST.get('psw')

#     mypatientdata=patient_a(patientֹID= patientֹID ,First_name=First_name,Last_name=Last_name,Phone_Number=Phone_Number1,Address=Address,Email_Address=Email_Address,Birth_Date=Birth_Date,password_patientֹ=password_patientֹ)
#     mypatientdata.save()
#     return render(requst,'patient_signup.html')


# def login_Doctor(requst):
#     return render(requst,'login_Doctor.html')

# def signup_Doctor(requst):
#     First_name=requst.POST.get('firstname')
#     print(First_name)
#     Last_name=requst.POST.get('lastname')
#     Phone_Number1=requst.POST.get('phone')
#     Address=requst.POST.get('Address')
#     Email_Address=requst.POST.get('email')
#     Birth_Date=requst.POST.get('birthday')
#     doctorID= requst.POST.get('DoctorId')
#     password_Doctor= requst.POST.get('psw')
   
#     mydoctordata=doctor_a(DoctorID= doctorID ,First_name=First_name,Last_name=Last_name,Phone_Number1=Phone_Number1,Address=Address,Email_Address=Email_Address,Birth_Date=Birth_Date,password_Doctor=password_Doctor)
#     mydoctordata.save()
#     return render(requst,'signup_Doctor.html')


# def login_patient(requst):
#     return render(requst,'login_patient.html')

# def AdminLogin (requst):
#     return render(requst,'AdminLogin.html')

# def AskDoctor (requst):
#     return render(requst,'AskDoctor.html')    


     