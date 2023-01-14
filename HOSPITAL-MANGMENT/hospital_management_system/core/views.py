from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView
from audioop import reverse
from django.views.generic import TemplateView
from .utils import Calendar
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta, date
import calendar
from django.urls import reverse
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
        if patient_a.objects.filter(patientֹID=p_id ,password_patientֹ=p_password ).exists():
            request.session['patient_id'] = p_id


            return redirect('patient_homepage')
        else: 
            return redirect('login_patient')
    else:
        return render(request, 'login_patient.html',{})






def patient_homepage(request):
    patient_id = request.session['patient_id']
    print(patient_id)
    patient = patient_a.objects.get(patientֹID=patient_id)
    print(patient)
    return render(request, 'patient_homepage.html', {'patient': patient})


def login_Doctor(request):
    if request.method == 'POST':
        doctor_id=request.POST['doc_id']
        dpctor_password=request.POST['doc_password']
        print(doctor_id,dpctor_password)
        
        if doctor_a.objects.filter(DoctorID=doctor_id ,password_Doctor=dpctor_password).exists():
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
        
        if hospital_admin.objects.filter(username=Admin_username ,password=Admin_password ).exists():
            return render(request,'admin_profile.html')
           
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

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

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



def after_request_ref(request,patient_id):
    patient = patient_a.objects.get(patientֹID = patient_id)
    return render(request,'after_request_ref.html', { 'patient':patient})  


def referrals_renewing(request,instance_id):
    instance = MedicalReferral.objects.get(pk=instance_id)
    instance.end_time  = instance.end_time + timedelta(days=90)
    instance.start_time= instance.start_time + timedelta(days=90)
    instance.save()
    return redirect('renwe_ref')

class renwe_ref(ListView):
    model = MedicalReferral
    template_name = 'renwe_ref.html'