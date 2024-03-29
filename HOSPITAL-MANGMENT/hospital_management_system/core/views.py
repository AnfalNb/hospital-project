from django.http import HttpResponse
from django.shortcuts import render
from .models import patient_a,doctor_a,hospital_admin, doctor_reply, doctor_shift_update
from .models import messages as message_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import patientform,doctorform,Message_form, doctor_shift_update_form
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView
from django.template import loader
import logging
from django.contrib import messages #import messages
import datetime
from django.db.models import Q
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

    if request.method == "POST":
        p_id = request.POST["p_id"]
        p_password = request.POST["p_password"]
        user = patient_a.objects.filter(patientID=p_id).first()
        if user is not None and user.password == p_password:
            request.session["user_id"] = user.id
            request.session["user_type"] = "patient"
            return render(request, "patient_homepage.html")
        else:
            return redirect("login_patient")
    else:
        return render(request, "login_patient.html", {})






def patient_homepage(request):
     return render(request,'patient_homepage.html')



def login_Doctor(request):
    if request.method == "POST":
        doctor_id = request.POST["doc_id"]
        dpctor_password = request.POST["doc_password"]
        user = doctor_a.objects.filter(DoctorID=doctor_id).first()
        if user is not None and user.password == dpctor_password:
            request.session["user_id"] = user.id
            request.session["user_type"] = "doctor"
            return render(request, "doctor_profile.html")
        else:
            return redirect("login_Doctor")
    else:
        return render(request, "login_Doctor.html", {})


def AdminLogin (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = hospital_admin.objects.filter(username=username).first()
        if user is not None and user.password == password:
            request.session["user_id"] = user.id
            request.session["user_type"] = "admin"
            return render(request, "admin_profile.html")
        else:
            context = {
                "result": "Username or password is not correct",
            }
            return render(request, "AdminLogin.html", context)
    else:
        return render(request, "AdminLogin.html", {})



def submitAskDoctor(request):
     if request.method == 'POST':
         form=doctorform(request.POST)
         if form.is_valid():
                 form.save()
                 return render(request, 'index.html')
         else:
             return render(request, 'index.html')
     else:
         return render(request, 'index.html',{})



def AskDoctor (request):
    if request.method == "POST":
        form = Message_form(request.POST)
        print(form.errors)
        if form.is_valid():
            message = form.save()
            message.doctorID = request.POST.get("doctorName", None)
            message.patientID = request.session.get("user_id", None)
            message.save()
            messages.success(request, "Message sent.")
            return render(request, "patient_homepage.html")
    names = doctor_a.objects.all()
    context = {
        "result2": names,
    }
    template = loader.get_template("AskDoctor.html")
    return render(request, "AskDoctor.html", context)
        # return render(request,'AskDoctor.html')

def reply_patients(request):
    user_id = request.session["user_id"]
    type = request.session["user_type"]
    user = None
    if type == "doctor":
        user = doctor_a.objects.get(id=user_id)
    questions = message_model.objects.filter(doctorID = user.id)
    print(questions)
    context = {
      "user": user,
      "questions": questions,
    }
    return render(request, "AnswerUrPatient.html", context)

def reply_patient(request, pk):
    question = message_model.objects.get(pk = pk)
    if request.method == "POST":
        doctor_reply.objects.create(
          message=question,
          answer=request.POST.get("answer", None)
        )
        return redirect("reply_patients")
    context = {
      "question": question,
    }
    return render(request, "reply_patient.html", context)


def patient_messages(request):
    user_id = request.session["user_id"]
    type = request.session["user_type"]
    user = None
    if type == "patient":
        user = doctor_a.objects.get(id=user_id)
    answers = doctor_reply.objects.filter(message__patientID = user.id)
    context = {
      "user": user,
      "answers": answers,
    }
    return render(request, "patient_messages.html", context)

def logout_view(request):
    request.session["user_id"] = None
    return redirect("/")



def admin_profile(request):
    return render(request,'admin_profile.html')



def doctor_profile(request):
    return render(request,'doctor_profile.html')


def logout_admin(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 
                             "successfully logged out")
    return redirect(render, 'logout_admin')


def shift_updates(request):
    if request.method == "POST":
        user_id = request.session["user_id"]
        type = request.session["user_type"]
        user = None
        if type == "doctor":
            user = doctor_a.objects.get(id=user_id)
        print(request.POST)
        form = doctor_shift_update_form(request.POST)
        if form.is_valid():
            shift_update = form.save(commit=False)
            shift_update.doctor = user
            date = request.POST["date"].split("-")
            time = request.POST["time"].split(":")
            shift_time = datetime.datetime(
                year=int(date[0]),
                month=int(date[1]),
                day=int(date[2]),
                hour=int(time[0]),
                minute=int(time[1]),
            )
            shift_update.time = shift_time
            shift_update.save()
            return redirect("doctor_profile")
    form = doctor_shift_update_form()
    context = {
      "form": form
    }
    return render(request, "send_update.html", context)

    
def admin_shift_updates(request):
    shift_updates = doctor_shift_update.objects.all()[:20]
    context = {
      "shift_updates": shift_updates
    }
    return render(request, "view_send_update.html", context)



class patientList(ListView):
    model = patient_a
    template_name = "patientList.html"
    
    def get_queryset(self):
        query = self.request.GET.get("query", None)
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
              Q(First_name__icontains = query) |
              Q(patientID__icontains = query) |
              Q(Last_name__icontains = query) |
              Q(Email_Address__icontains = query)
            )
        return queryset


class DoctorList(ListView):
    model = doctor_a
    template_name = 'AskDoctor.html'




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


 # # if request.method== 'GET':
    # if request.method == 'POST':
    #     p_id=request.POST['p_id']
    #     p_password=request.POST['p_password']
    #     print(p_id,p_password)
    #     patient_user = patient_a.objects.get(patientֹID=p_id,password_patientֹ=p_password)
    #     # p_user=authenticate(patientֹID=p_id ,password_patientֹ=p_password )
    #     print(patient_user)
    #     if patient_user is not None:
    #        login(request, patient_user)
    #        return redirect('patient_homepage')
            
    #     else: 
    #         return redirect('login_patient')
    # else:
    #     return render(request, 'login_patient.html',{})
            # context={"error": "Invalid id patient"}
            # return HttpResponse("<h1>//////////// hospital mangment system website")
            # render(request, 'login_patient.html',context)
        
        # return redirect('patient_homepage.html')
#    return render(request, 'login_patient.html',{})




