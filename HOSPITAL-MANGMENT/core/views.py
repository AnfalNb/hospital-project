from audioop import reverse
from django.http import Http404, HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView,UpdateView
from django.template.loader import render_to_string
from datetime import datetime, timedelta, date
from .utils import Calendar
from django.urls import reverse
import calendar
from django.utils.safestring import mark_safe
from django.views import generic





# import django.contrib.auth as auth
# Create your views here.

def index(requst):
    return render(requst, 'index.html')


def signup_patient(request):
    form=signuppatientform(request.POST or None)
    print("requst here!!!")
    if form.is_valid():
            form.save()
            return redirect('login_patient')

    context={'form':form}
    return render(request, 'signup_patient.html',context)

# def update_patient(request,patientֹID): #not completed 
#     patient=patient_a.objects.get(pk=patientֹID)
#     form=patientform(request.POST or None,instance=patient)
#     if form.is_valid(): 
#             form.save()
#             return redirect('')
#     return render(request, 'signup_patient.html',{'patient':patient,'form':form })


def Doctor_signup(request):
    form=doctorform(request.POST )
    if form.is_valid():
            form.save()
            return redirect('login_Doctor')

            # return render(request, 'login_Doctor.html')

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
            # return render(request,'patient_homepage.html')
            request.session['patient_id'] = p_id
            return redirect('patient_homepage')
        else: 
            messages.error(request, 'Invalid patient ID or password')

            return redirect('login_patient')
    else:
        return render(request, 'login_patient.html',{})








def patient_homepage(request):
    # Get the patient's ID from the session data
    patient_id = request.session['patient_id']
    # Retrieve the patient's data from the database
    patient = patient_a.objects.get(patientֹID=patient_id)
    # Render the profile page with the patient's data
    return render(request, 'patient_homepage.html', {'patient': patient})





def login_Doctor(request):
    if request.method == 'POST':
        doctor_id=request.POST['doc_id']
        dpctor_password=request.POST['doc_password']
        print(doctor_id,dpctor_password)
        #patient_user = get_object_or_404(patient_a,patientֹID=p_id,password_patientֹ=p_password)
        #patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
        #p_user=patient_a.objects.get(patientֹID=p_id ,password_patientֹ=p_password ).exists()
        if doctor_a.objects.filter(DoctorID=doctor_id ,password_Doctor=dpctor_password).exists():
            # return render(request,'doctor_profile.html')
            request.session['DoctorID'] = doctor_id

            return redirect('doctor_profile')
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
            # return render(request,'admin_profile.html')
            return redirect('admin_profile')
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
    doctor_id = request.session['DoctorID']
    doctor = doctor_a.objects.get(DoctorID=doctor_id)
    return render(request, 'doctor_profile.html', {'doctor': doctor})


class patientList(ListView):
    model = patient_a
    template_name = 'patientList.html'
class doctorList(ListView):
    model = doctor_a
    template_name = 'doctorList.html'
def userslist(request):
    return render(request,'userslist.html')


def update_patient(request, patient_id):
    patient = patient_a.objects.get(pk=patient_id)  # Retrieve the patient instance from the database
    if request.method == 'POST':
        form = patientform(request.POST, instance=patient)  # Pass the patient instance to the form
        if form.is_valid():
            form.save()  # Save the form to update the patient instance in the database
            return redirect('patient_homepage')  # Redirect to the homepage after the update is successful
    else:
        form = patientform(instance=patient)  # Create the form with the patient instance data
    return render(request, 'update_patient.html', {'form': form, 'patient': patient})





def update_doctor(request, doctor_id):
    doctor = doctor_a.objects.get(pk=doctor_id)  # Retrieve the doctor instance from the database
    if request.method == 'POST':
        form = doctorupdateform(request.POST, instance=doctor)  # Pass the doctor instance to the form
        if form.is_valid():
            form.save()  # Save the form to update the doctor instance in the database
            return redirect('doctor_profile')  # Redirect to the doctor list page after the update is successful
    else:
        form = doctorupdateform(instance=doctor)  # Create the form with the doctor instance data
    return render(request, 'update_doctor.html', {'form': form, 'doctor': doctor})    


from django.views.generic import TemplateView

class doctorDetailView(TemplateView):
    template_name = 'doctor_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Doctor'] = doctor_a.objects.get(pk=kwargs['DoctorID'])
        return context


def delete_doctor(request, id):
    obj =doctor_a.objects.get(pk=id)
    obj.delete()
    return redirect('doctorList')


def delete_patient(request, id):
    obj =patient_a.objects.get(pk=id)
    obj.delete()
    return redirect('patientList')



# def search_doctor(request):
#     query = request.GET.get('q')
#     results = doctor_a.objects.filter(First_name__contains=query)
#     return render(request, 'search_results.html', {'results': results})

def search_doctor(request):
    query = request.GET.get('q')
    if query is not None:
        results = doctor_a.objects.filter(First_name__contains=query)
        return render(request, 'search_result.html', {'results': results})
    else:
        return render(request, 'search_doctor.html')

#help function
def help_logout_doctor(requst):
    return render(requst,'doctor_logout.html')

def logout_doctor(request):
    logout(request)
    # Redirect to a success page.
    return redirect('index')

#======================================================================ASIA
 

class patientList(ListView):
    model = patient_a
    template_name = 'patientList.html'




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



def error_page(request):
    return render(request, 'error.html')



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


    #---------------------------------------------------------------------------------

import datetime
def patienttListinDoctor(request):
   # retrieve all appointments for the patient
    doctor_id = request.session['DoctorID']
    doctor = doctor_a.objects.get(DoctorID=doctor_id)
    today_appointments = patientAppointment.objects.filter(Date =  datetime.datetime.now(),DoctorName =doctor.First_name)
    # patient = patient_a.objects.get(pk=patient_id)

    context = {'appointments': today_appointments}
    return render(request, 'patienttListinDoctor.html', context)
#----------------------------------------------------------------------------
class test_blood(ListView):
    model = TestBlood
    template_name = 'test_blood.html'


class test_blood_details(TemplateView):
    template_name = 'test_blood_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Blood'] = TestBlood.objects.get(pk=kwargs['test_number'])
        return context   
class CalendarView(generic.ListView):
    model = EVENT_CAL
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

from datetime import date
def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return date.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = EVENT_CAL()
    if event_id:
        instance = get_object_or_404(EVENT_CAL, pk=event_id)
    else:
        instance = EVENT_CAL()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event.html', {'form': form})       


#log out for patient
def logout_patient_accepted(request):
    return render(request,'logout_patient_accepted.html')

def logout_patient(request):
    logout(request)
    # Redirect to a success page.
    return redirect('index')


def referral(request, patient_id):
    refs = MedicalReferral.objects.filter(patient_id=patient_id)
    patient = patient_a.objects.get(pk =patient_id)
    return render(request, 'referral.html', {'refs': refs, 'patient':patient})


def after_request_ref(request,patient_id,refpk):
    ref = MedicalReferral.objects.filter(patient_id=patient_id,pk=refpk).update(renewed=1) 

    # print(str(ref.renewed))
    patient = patient_a.objects.get(patientֹID = patient_id)
    return render(request,'after_request_ref.html', { 'patient':patient})  


def referrals_renewing(request,instance_id):
    instance = MedicalReferral.objects.get(pk=instance_id)
    instance.end_time  = instance.end_time + timedelta(days=90)
    instance.start_time= instance.start_time + timedelta(days=90)
    instance.save()
    return redirect('renwe_ref')

# class renwe_ref(ListView):
#     model = MedicalReferral
#     template_name = 'renwe_ref.html'

def renwe_ref(request):
    doctor_id = request.session['DoctorID']
    doctor = doctor_a.objects.get(DoctorID=doctor_id)
    new_referral = MedicalReferral.objects.filter(doctor_name=doctor.First_name,renewed=1)
    # doctor = doctor_a.objects.get(pk =doctor_name)
    return render(request, 'renwe_ref.html', {'new_referral': new_referral })


def receving_work(request, doctor_name):
    receiving = EVENT_CAL.objects.filter(doctor_name=doctor_name)
    doctor = doctor_a.objects.get(First_name =doctor_name)
    return render(request, 'receving_work.html', {'receiving': receiving, 'doctor':doctor})    