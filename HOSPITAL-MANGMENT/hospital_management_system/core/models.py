from django.db import models

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
          return self.test_number

















