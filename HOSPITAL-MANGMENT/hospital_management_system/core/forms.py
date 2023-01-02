from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from .models import patient_a,doctor_a

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

class WorkScheduleForm(forms.ModelForm):
    visible_for=forms.CharField(required=False)
    editable_by=forms.CharField(required=False)
    class Meta:
        model=WorkSchedule
        fields=['owner','visible_for','editable_by']
        # fields = '__all__'

    def save(self,commit=True):
        WorkSchedule=self.instance
        for email in self.cleaned_data['visible_for'].split(";"):
            if doctor_a.objects.filter(Email_Address=email).exists():
                WorkSchedule.visible_for.add(email)
        for email in self.cleaned_data['editable_by'].split(";"):
            if doctor_a.objects.filter(Email_Address=email).exists():
                WorkSchedule.visible_for.add(email)   

        if commit:
            WorkSchedule.save()

        return WorkSchedule

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=[]