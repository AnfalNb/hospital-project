from django.forms import ModelForm 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import patient_a,doctor_a,summary_a



class patientform(forms.ModelForm):
    class Meta:
        model=patient_a
        fields= [
            'patientֹID','First_name','Last_name','Phone_Number','Address','Email_Address','Birth_Date','password_patientֹ'
            ]


class doctorform(forms.ModelForm):
    class Meta:
        model=doctor_a
        fields= [
            'DoctorID','First_name','Last_name','Phone_Number1','Address','Email_Address','Birth_Date','Medical_Field','File_Diploma','password_Doctor'
            ]

# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model=Appointment
#         fields= ['DoctorName','medical_field','Date','time']

#         labels ={
#             'DoctorName' : 'Doctor Name' ,
#             'medical_field': 'medical_field',
#             'Date':'Date',
#             'time':'time',
            

#         }
#         widgets = {

#            'DoctorName'  : forms.TextInput(attrs={'class':'form-control'}),
#            'medical_field': forms.TextInput(attrs={'class':'form-control'}),
#            'Date':forms.DateInput(attrs={'class':'form-control'}),
#            'time' :forms.TimeInput(attrs={'class':'form-control'}),


#         }



class AppointmentForm(forms.ModelForm):
    class Meta:
        model=patientAppointment
        fields= ['DoctorName','medical_field','Date','time','patient']
        labels ={
            'DoctorName' : 'Doctor Name' ,
            'medical_field': 'medical_field',
            'Date':'Date',
            'time':'time',
        }
        widgets = {
           'DoctorName'  : forms.TextInput(attrs={'class':'form-control'}),
           'medical_field': forms.TextInput(attrs={'class':'form-control'}),
           'Date':forms.DateInput(attrs={'class':'form-control'}),
           'time' :forms.TimeInput(attrs={'class':'form-control'}),
        }

class updateAppointmentForm(forms.ModelForm):
    class Meta:
        model=patientAppointment
        fields= ['DoctorName','medical_field','Date','time']
        labels ={
            'DoctorName' : 'Doctor Name' ,
            'medical_field': 'medical_field',
            'Date':'Date',
            'time':'time',
        }
        widgets = {
           'DoctorName'  : forms.TextInput(attrs={'class':'form-control'}),
           'medical_field': forms.TextInput(attrs={'class':'form-control'}),
           'Date':forms.DateInput(attrs={'class':'form-control'}),
           'time' :forms.TimeInput(attrs={'class':'form-control'}),
        }




        

class summrayForm(forms.ModelForm):

    class Meta:
         model=summary_a
         fields= [
             'patient_id','date','title','body'
            ]
