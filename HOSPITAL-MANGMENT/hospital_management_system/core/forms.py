from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
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


class EventForm(ModelForm):
  class Meta:
    model = EVENT_CAL
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)