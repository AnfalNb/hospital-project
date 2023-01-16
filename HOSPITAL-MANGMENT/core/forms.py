from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import patient_a,doctor_a
from django.forms import ModelForm, DateInput


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
        # labels ={
        #     'DoctorID' : 'ID' ,
        #     'First_name': 'First name',
        #     'Last_name':'Last name',
        #     'Phone_Number1':'Phone Number',
        #     'Address':  'Address',
        #    ' Email_Address': 'Email Address',
        #     'Birth_Date':'Birth Date:',
        #     'Medical_Field' : 'Medical_Field',
        #     'File_Diploma' : 'File Diploma',
        #     'password_Doctor': 'password',
        # }
        # widgets = {
        #     'DoctorID' : forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        #     'First_name': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
        #     'Last_name':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
        #     'Phone_Number1':forms.TextInput(attrs={'class':'form-control'}),
        #     'Address': forms.TextInput(attrs={'class':'form-control'}),
        #    ' Email_Address': forms.EmailInput(attrs={'class':'form-control'}),
        #     'Birth_Date':forms.DateInput(attrs={'class':'form-control','readonly':'readonly'}),
        #     'Medical_Field': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
        #     'File_Diploma': forms.FileInput(attrs={'class':'form-control'}),

        #     'password_Doctor': forms.TextInput(attrs={'class':'form-control','type': "password"}),


        # }

class doctorupdateform(forms.ModelForm):
    class Meta:
        model=doctor_a
        fields= [
            'DoctorID','First_name','Last_name','Phone_Number1','Address','Email_Address','Birth_Date','Medical_Field','password_Doctor'
    
            ]
        labels ={
            'DoctorID' : 'ID' ,
            'First_name': 'First name',
            'Last_name':'Last name',
            'Phone_Number1':'Phone Number',
            'Address':  'Address',
           ' Email_Address': 'Email Address',
            'Birth_Date':'Birth Date:',
            'Medical_Field' : 'Medical_Field',
            'password_Doctor': 'password',
        }
        widgets = {
            'DoctorID' : forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'First_name': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Last_name':forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Phone_Number1':forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
           ' Email_Address': forms.EmailInput(attrs={'class':'form-control'}),
            'Birth_Date':forms.DateInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Medical_Field': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
            'password_Doctor': forms.TextInput(attrs={'class':'form-control','type': "password"}),


        }

class signuppatientform(forms.ModelForm):
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
            'patientֹID' : forms.TextInput(attrs={'class':'form-control'}),
            'First_name': forms.TextInput(attrs={'class':'form-control'}),
            'Last_name':forms.TextInput(attrs={'class':'form-control'}),
            'Phone_Number':forms.TextInput(attrs={'class':'form-control'}),
            'Address': forms.TextInput(attrs={'class':'form-control'}),
           ' Email_Address': forms.EmailInput(attrs={'class':'form-control'}),
            'Birth_Date':forms.DateInput(attrs={'class':'form-control'}),
            'password_patientֹ': forms.TextInput(attrs={'class':'form-control','type': "password"}),

        }
    


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