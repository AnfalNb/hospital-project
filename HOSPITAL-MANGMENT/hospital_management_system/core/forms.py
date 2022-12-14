from django.forms import ModelForm
from .models import *

class NewdoctorsForm(ModelForm):
    class Meta:
        model=doctors
        fields=['first name']

class NewppatientForm(ModelForm):
    class Meta:
        model=patient
        fields=['first name']        