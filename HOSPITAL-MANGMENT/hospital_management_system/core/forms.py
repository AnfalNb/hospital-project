from django.forms import ModelForm
from .models import *


class NewdoctorsForm(ModelForm):
    class Meta:
        model=doctor
        fields=['first name']

class NewppatientForm(ModelForm):
    class Meta:
        model=patient_a
        fields=['first name']



