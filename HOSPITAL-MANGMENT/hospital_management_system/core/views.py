from django.http import HttpResponse
from django.shortcuts import render
from .models import patient_a,doctor_a,hospital_admin,Appointment
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import patientform,doctorform,AppointmentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView

# import django.contrib.auth as auth
# Create your views here.

def index(requst):
    return render(requst, 'index.html')


def signup_patient(request):
    form=patientform(request.POST or None)
    print("requst here!!!")
    if form.is_valid():
            form.save()
            return render(request, 'login_patient.html')

    context={'form':form}
    return render(request, 'signup_patient.html',context)

def update_patient(request,patientֹID): #not completed 
    patient=patient_a.objects.get(pk=patientֹID)
    form=patientform(request.POST or None,instance=patient)
    if form.is_valid(): 
            form.save()
            return redirect('')
    return render(request, 'signup_patient.html',{'patient':patient,'form':form })


def Doctor_signup(request):
    form=doctorform(request.POST )
    if form.is_valid():
            form.save()
            return render(request, 'login_Doctor.html')

    context={'form':form}
    return render(request, 'Doctor_signup.html',context)

def login_patient(request):

    if request.method == 'POST':
        p_id=request.POST['p_id']
        p_password=request.POST['p_password']
        print(p_id,p_password)
        #patient_user = get_object_or_404(patient_a,patientֹID=p_id,password_patientֹ=p_password)
        #patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
        #p_user=patient_a.objects.get(patientֹID=p_id ,password_patientֹ=p_password ).exists()
        if patient_a.objects.filter(patientֹID=p_id ,password_patientֹ=p_password ).exists():
            return render(request,'patient_homepage.html')
           #return redirect('patient_homepage')
        else: 
            return redirect('login_patient')
    else:
        return render(request, 'login_patient.html',{})






def patient_homepage(request):
     return render(request,'patient_homepage.html')



def login_Doctor(request):
    if request.method == 'POST':
        doctor_id=request.POST['doc_id']
        dpctor_password=request.POST['doc_password']
        print(doctor_id,dpctor_password)
        #patient_user = get_object_or_404(patient_a,patientֹID=p_id,password_patientֹ=p_password)
        #patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
        #p_user=patient_a.objects.get(patientֹID=p_id ,password_patientֹ=p_password ).exists()
        if doctor_a.objects.filter(DoctorID=doctor_id ,password_Doctor=dpctor_password).exists():
            return render(request,'doctor_profile.html')
           #return redirect('patient_homepage')
        else: 
            return redirect('login_Doctor')
    else:
        return render(request, 'login_Doctor.html',{})


def AdminLogin (request):
    if request.method == 'POST':
        Admin_username=request.POST['username']
        Admin_password=request.POST['password']
        print(Admin_username,Admin_password)
        #patient_user = get_object_or_404(patient_a,patientֹID=p_id,password_patientֹ=p_password)
        #patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
        #p_user=patient_a.objects.get(patientֹID=p_id ,password_patientֹ=p_password ).exists()
        if hospital_admin.objects.filter(username=Admin_username ,password=Admin_password ).exists():
            return render(request,'admin_profile.html')
           #return redirect('patient_homepage')
        else: 
            return redirect('AdminLogin')
    else:
        return render(request, 'AdminLogin.html',{})


def AskDoctor (requst):
    return render(requst,'AskDoctor.html')    



def logout_view(request):
    logout(request)
    return redirect(request,index)


def admin_profile(request):
    return render(request,'admin_profile.html')
    
def doctor_profile(request):
    return render(request,'doctor_profile.html')
#=============================================================================================================================
# def Doctor_signup(requst):
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
#     return render(requst,'Doctor_signup.html')



# def login_patient(requst):
#     return render(requst,'login_patient.html')




 

class patientList(ListView):
    model = patient_a
    template_name = 'patientList.html'





 




   



# def appointment_list(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AppointmentForm()
#     appointments = Appointment.objects.all()
#     return render(request, 'appointment_list.html', {'form': form, 'appointments': appointments})



class appointmentList(ListView):
    model = Appointment
    template_name = 'appointment_list.html'



#---------------------------------------------------------------------------------


def add_appointments(request):
    form=AppointmentForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('appointmentList')

    context={'form':form}
    return render(request, 'add_appointments.html',context)


def delete_appointment(request, id):
    obj =Appointment.objects.get(pk=id)
    obj.delete()
    return redirect('appointmentList')