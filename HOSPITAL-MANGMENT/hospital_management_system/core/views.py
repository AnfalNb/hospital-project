from audioop import reverse
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import patient_a,doctor_a,hospital_admin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import doctorupdateform, patientform,doctorform
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView,UpdateView
from django.template.loader import render_to_string


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
            request.session['doctor_id'] = doctor_id

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
    doctor_id = request.session['doctor_id']
    doctor = doctor_a.objects.get(DoctorID=doctor_id)
    return render(request, 'doctor_profile.html', {'doctor': doctor})

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

