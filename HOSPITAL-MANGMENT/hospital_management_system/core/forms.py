from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import patient_a

class patientform(forms.ModelForm):
    class Meta:
        model=patient_a
        fields= [
            'patientֹID','First_name','Last_name','Phone_Number','Address','Email_Address','Birth_Date','password_patientֹ'
            ]


