from django.http import HttpResponse
from django.shortcuts import render
from .models import patient_a,doctor_a,hospital_admin,patientAppointment,summary_a
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import patientform,doctorform,AppointmentForm,updateAppointmentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView
from .forms import summrayForm

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
        p_id = request.POST['p_id']
        p_password = request.POST['p_password']
        # Check if the provided ID and password match a patient in the database
        if patient_a.objects.filter(patientֹID=p_id, password_patientֹ=p_password).exists():
            # Store the patient's ID in the session data
            request.session['patient_id'] = p_id
            # Redirect to the patient's homepage
            return redirect('patient_homepage')
        else: 
            messages.error(request, 'Invalid patient ID or password')
            return redirect('login_patient')
    else:
        return render(request, 'login_patient.html', {})

def patient_homepage(request):
    # Get the patient's ID from the session data
    patient_id = request.session['patient_id']
    print(patient_id)
    patient = patient_a.objects.get(patientֹID=patient_id)
    print(patient)
    return render(request, 'patient_homepage.html', {'patient': patient})


# def login_patient(request):

#     if request.method == 'POST':
#         p_id=request.POST['p_id']
#         p_password=request.POST['p_password']
#         print(p_id,p_password)
#         #patient_user = get_object_or_404(patient_a,patientֹID=p_id,password_patientֹ=p_password)
#         #patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
#         #p_user=patient_a.objects.get(patientֹID=p_id ,password_patientֹ=p_password ).exists()
#         if patient_a.objects.filter(patientֹID=p_id ,password_patientֹ=p_password ).exists():
#             request.session['patientID'] = p_id

#             # return render(request,'patient_homepage.html')
#             return redirect('patient_homepage')
#         else: 
#             return redirect('login_patient')
#     else:
#         return render(request, 'login_patient.html',{})



       
# def login_patient(request):
#     if request.method == 'POST':
#         p_id = request.POST['p_id']
#         p_password = request.POST['p_password']
#         # Check if the provided ID and password match a patient in the database
#         if patient_a.objects.filter(patientID=p_id, password_patient=p_password).exists():
#             # Store the patient's ID in the session data
#             request.session['patient_'] = p_id
#             # Redirect to the patient's homepage
#             return redirect('patient_homepage')
#         else: 
#             messages.error(request, 'Invalid patient ID or password')
#             return redirect('login_patient')
#     else:
#         return render(request, 'login_patient.html', {})

# def patient_homepage(request):
#     # Get the patient's ID from the session data
#     patient_id = request.session['patient_id']
#     # Retrieve the patient's data from the database
#     patient = patient_a.objects.get(patient_ID=patient_id)
#     # Render the profile page with the patient's data
#     return render(request, 'patient_homepage.html', {'patient': patient})
# def login_patient(request):

#     if request.method == 'POST':
#         p_id=request.POST['p_id']
#         p_password=request.POST['p_password']
#         print(p_id,p_password)
#         #patient_user = get_object_or_404(patient_a,patientֹID=p_id,password_patientֹ=p_password)
#         #patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
#         #p_user=patient_a.objects.get(patientֹID=p_id ,password_patientֹ=p_password ).exists()
#         if patient_a.objects.filter(patientֹID=p_id ,password_patientֹ=p_password ).exists():
#             # return render(request,'patient_homepage.html')
#             request.session['patient_id'] = p_id
#             return redirect('patient_homepage')
#         else: 
#             messages.error(request, 'Invalid patient ID or password')

#             return redirect('login_patient')
#     else:
#         return render(request, 'login_patient.html',{})


# def patient_homepage(request):
#     # Get the patient's ID from the session data
#     patient_id = request.session['patient_id']
#     # Retrieve the patient's data from the database
#     patient = patient_a.objects.get(patientֹID=patient_id)
#     # Render the profile page with the patient's data
#     return render(request, 'patient_homepage.html', {'patient': patient})


# def patient_homepage(request):
#     # Get the patient's ID from the session data
#     patient_id = request.session['patientID']
#     # Retrieve the patient's data from the database
#     patient = patient_a.objects.get(patientֹID=patient_id)
#     # Render the profile page with the patient's data
#     return render(request, 'patient_homepage.html', {'patient': patient})
# def patient_homepage(request):
#      return render(request,'patient_homepage.html')



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



# class appointmentList(ListView):
#     model = patientAppointment
#     template_name = 'appointment_list.html'

from django.shortcuts import  get_object_or_404

def appointmentList(request, patient_id):
   # retrieve all appointments for the patient
    patient_appointments = patientAppointment.objects.filter(patient=patient_id)
    patient = patient_a.objects.get(pk=patient_id)

    context = {'appointments': patient_appointments,'patient':patient}
    return render(request, 'appointment_list.html', context)

# #---------------------------------------------------------------------------------


def add_appointments(request,p_id):
    form=AppointmentForm(request.POST)
    if form.is_valid():
            form.save()
            return redirect('appointmentList',p_id)

    context={'form':form}
    return render(request, 'add_appointments.html',context)


# def delete_appointment(request, id):
#     obj =patientAppointment.objects.get(pk=id)
#     obj.delete()
#     return redirect('appointmentList')
def error_page(request):
    return render(request, 'error.html')

# def delete_appointment(request, id,p_id):
#     try:
#         obj =patientAppointment.objects.get(pk=id)
#         print(obj)
#         obj.delete()
#     except patientAppointment.DoesNotExist:
#         return redirect('error_page')
#     return redirect('appointmentList', patient_id=p_id)

def delete_appointment(request, id,p_id):
    obj =patientAppointment.objects.get(pk=id)
    obj.delete()
    return redirect('appointmentList',p_id)


def update_Appointment(request, Appointment_pk, p_id):
    try:
        appoint = patientAppointment.objects.get(pk=Appointment_pk)  # Retrieve the patient instance from the database
    except patientAppointment.DoesNotExist:
        # handle the error
        return redirect('error_page')
    if request.method == 'POST':
        form = updateAppointmentForm(request.POST, instance=appoint)  # Pass the patient instance to the form
        if form.is_valid():
            form.save()  # Save the form to update the patient instance in the database
            return redirect('appointmentList' ,p_id)  # Redirect to the homepage after the update is successful
    else:
        form = updateAppointmentForm(instance=appoint)  # Create the form with the patient instance data
    return render(request, 'update_Appointment.html', {'form': form, 'Appointment': appoint})

#----------------------summary--------------------------
def send_summray(request):
    form=summrayForm(request.POST )
    if form.is_valid():
            form.save()
            return render(request, 'send_summary.html')

    context={'form':form}
    return render(request, 'send_summary.html',context)




from django.views.generic import TemplateView

class summry_views(TemplateView):
    model=summary_a
    template_name = 'summry_views.html'

def view_summary(request, patient_id):
    summ = summary_a.objects.get(patient_id=patient_id)
    patient = patient_a.objects.get(pk=patient_id)

    return render(request, 'summry_views.html', {'summ': summ,'patient': patient})