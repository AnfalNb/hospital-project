from django.db import models
from django.urls import reverse
# Create your models here.

# python classes for database
class doctor_a(models.Model):
    DoctorID=models.CharField(max_length=20,null = True)
    First_name=models.CharField(max_length=20,null = True)
    Last_name=models.CharField(max_length=20,null = True)
    Phone_Number1=models.CharField(max_length=20, null=True)
    Address=models.CharField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    Birth_Date=models.DateField(null=True)
    Medical_Field=models.CharField(max_length=20,null=True)
    File_Diploma=models.FileField(blank=True,null=True)
    password_Doctor=models.CharField(max_length=20,null = True)


    class Meta:
        db_table = 'doctor_a'

    def __str__(self):
          return str(self.First_name)
    
class patient_a(models.Model):
    patientֹID=models.CharField(max_length=20,null = True)
    First_name=models.CharField(max_length=20,null = True)
    Last_name=models.CharField(max_length=20,null = True)
    Phone_Number=models.CharField(max_length=10,null=True)
    Address=models.TextField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    Birth_Date=models.DateField(null=True)
    password_patientֹ=models.CharField(max_length=20,null = True)

    class Meta:
        db_table = 'patient_a'

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


class EVENT_CAL(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    doctor_name=models.ForeignKey(doctor_a, on_delete=models.CASCADE)
    class Meta:
        db_table = 'EVENT_CAL'
    @property
    def get_html_url(self):
        re_path = reverse('event_edit', args=(self.id,))
        return f'<a href="{re_path}"> {self.title} </a>'














