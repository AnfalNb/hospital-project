from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(doctor_a) 
admin.site.register(patient_a)
admin.site.register(hospital_admin)
# admin.site.register(Appointment)
admin.site.register(patientAppointment)
admin.site.register(summary_a)