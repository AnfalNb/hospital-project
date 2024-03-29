from audioop import reverse
from django.db import models

# Create your models here.

# python classes for database
class doctor_a(models.Model):
    DoctorID=models.CharField(max_length=9, primary_key=True)
    First_name=models.CharField(max_length=20,null = True)
    Last_name=models.CharField(max_length=20,null = True)
    Phone_Number1=models.CharField(max_length=10, null=True)
    Address=models.CharField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    Birth_Date=models.DateField(null=True)
    Medical_Field=models.CharField(max_length=20,null=True)
    File_Diploma=models.FileField(blank=True,null=True)
    password_Doctor=models.CharField(max_length=20,null = True)


    class Meta:
        db_table = 'doctor_a'

    
    
class patient_a(models.Model):
    patientֹID=models.CharField(max_length=20,primary_key=True)
    First_name=models.CharField(max_length=20,null = True)
    Last_name=models.CharField(max_length=20,null = True)
    Phone_Number=models.CharField(max_length=10,null=True)
    Address=models.TextField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    Birth_Date=models.DateField(null=True)
    password_patientֹ=models.CharField(max_length=20,null = True)

    class Meta:
        db_table = 'patient_a'
    def __str__(self):
        return self.patientֹID

class hospital_admin(models.Model):
    username=models.CharField(max_length=30,null = True)
    password=models.CharField(max_length=30,null=True)
    class Meta:
        db_table = 'hospital_admin'

class messages(models.Model): #patient messages
    patientֹName=models.CharField(max_length=20,null = True)
    matter=models.CharField(max_length=10,null=True)
    message=models.TextField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    



    class Meta:
        db_table = 'messages'

#=========================================================================================
class patientAppointment(models.Model):
    DoctorName=models.CharField(max_length=30,null=True)
    medical_field=models.CharField(max_length=30,null=True)
    Date=models.DateField(null=True)
    time=models.TimeField(null=True)
    patient = models.CharField(max_length=30,null=True)
    class Meta:
        db_table = 'patientAppointment'


class summary_a(models.Model):
    patient_id=models.CharField(max_length=30,null=True)
    date=models.DateField(null=True)
    title=models.CharField(max_length=30,null=True)
    body=models.TextField(max_length=300,null=True)
    class Meta():
        db_table='summary_a'
#============================================================================================

class TestBlood(models.Model):
    date_test=models.DateField(null=True)
    laboratory_field=models.CharField(max_length=30)
    referring_doctor=models.CharField(max_length=30)
    test_number=models.CharField(max_length=25,primary_key=True)
    name_test=models.CharField(max_length=30)
    result=models.CharField(max_length=30)
    class Meta:
        db_table = 'TestBlood'

        def __str__(self):
          return str(self.test_number)


from django.urls import reverse

class EVENT_CAL(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doctor_name=models.CharField(max_length=200)
    class Meta:
        db_table = 'EVENT_CAL'

    @property
    def get_html_url(self):
        re_path = reverse('event_edit', args=(self.id,))
        return f'<a href="{re_path}"> {self.title} </a>'

    def __str__(self):
          return str(self.title)



class MedicalReferral(models.Model):
    name_referral = models.CharField(max_length=200)
    start_time = models.DateField()
    end_time = models.DateField()
    patient_id=models.CharField(max_length=10)
    doctor_name=models.CharField(max_length=200)
    renewed = models.CharField(max_length = 1)

    class Meta:
        db_table = 'MedicalReferral' 

    def __str__(self):
          return str(self.patient_id)

