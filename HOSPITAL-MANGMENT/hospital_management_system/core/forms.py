from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import patient_a,doctor_a

class patientform(forms.ModelForm):
    class Meta:
        model=patient_a
        fields= [
            'patientֹID','First_name','Last_name','Phone_Number','Address','Email_Address','Birth_Date','password_patientֹ'
            ]
        labels ={
            'patientֹID' : 'ID' ,
            'First_name': 'First name',
            'Last_name':'Last name',
            'Phone_Number':'Phone Number',
            'Address':  'Address',
           ' Email_Address': 'Email Address',
            'Birth_Date':'Birth Date:',
            'password_patientֹ': 'password',
        }
        widgets = {
            'patientֹID' : forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'First_name': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Last_name':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Phone_Number':forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
           ' Email_Address': forms.EmailInput(attrs={'class':'form-control'}),
            'Birth_Date':forms.DateInput(attrs={'class':'form-control','readonly':'readonly'}),
            'password_patientֹ': forms.TextInput(attrs={'class':'form-control','type': "password"}),

        }

class doctorform(forms.ModelForm):
    class Meta:
        model=doctor_a
        fields= [
            'DoctorID','First_name','Last_name','Phone_Number1','Address','Email_Address','Birth_Date','Medical_Field','File_Diploma','password_Doctor'
            ]

