from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import patient_a,doctor_a

class patientform(forms.ModelForm):
    class Meta:
        model = patient_a
        fields = [
            "patientID",
            "First_name",
            "Last_name",
            "Phone_Number",
            "Address",
            "Email_Address",
            "Birth_Date",
            "password",
        ]


class doctorform(forms.ModelForm):
    class Meta:
        model = doctor_a
        fields = [
            "DoctorID",
            "First_name",
            "Last_name",
            "Phone_Number1",
            "Address",
            "Email_Address",
            "Birth_Date",
            "Medical_Field",
            "File_Diploma",
            "password",
        ]
 

class Message_form(forms.ModelForm):
    class Meta:
        model = messages
        fields = ["patientName", "Email_Address", "matter", "doctorName", "message"]

