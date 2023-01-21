from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

# python classes for database
class doctor_a(AbstractBaseUser):
    DoctorID = models.CharField(max_length=255, null=True)
    First_name = models.CharField(max_length=255, null=True)
    Last_name = models.CharField(max_length=255, null=True)
    Phone_Number1 = models.CharField(max_length=255, null=True)
    Address = models.TextField(null=True)
    Email_Address = models.EmailField(max_length=255, null=True)
    Birth_Date = models.DateField(null=True, blank=True)
    Medical_Field = models.CharField(max_length=255, null=True)
    File_Diploma = models.FileField(blank=True, null=True)
    # password_Doctor = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "DoctorID"

    class Meta:
        db_table = "doctor_a"


class patient_a(AbstractBaseUser):
    patientID = models.CharField(max_length=255, null=True)
    First_name = models.CharField(max_length=255, null=True)
    Last_name = models.CharField(max_length=255, null=True)
    Phone_Number = models.CharField(max_length=255, null=True)
    Address = models.TextField(null=True)
    Email_Address = models.EmailField(max_length=255, null=True)
    Birth_Date = models.DateField(null=True, blank=True)
    # password_patientֹ = models.CharField(max_length=255, null=True)
    USERNAME_FIELD = "patientID"

    class Meta:
        db_table = "patient_a"


class hospital_admin(AbstractBaseUser):
    username = models.CharField(max_length=255, null=True)
    # password = models.CharField(max_length=30, null=True)
    USERNAME_FIELD = "username"

    class Meta:
        db_table = "hospital_admin"



class messages(models.Model):  # patient messages
    patientName = models.CharField(max_length=255, null=True)
    Email_Address = models.CharField(max_length=255, null=True)
    matter = models.CharField(max_length=255, null=True)
    doctorName = models.CharField(max_length=255, null=True)
    doctorID = models.CharField(max_length=255, null=False)
    patientID = models.CharField(max_length=255, null=False)
    message = models.TextField(max_length=500, null=True)

    class Meta:
        db_table = "messages"


class doctor_reply(models.Model):  # patient messages
    message = models.ForeignKey(messages, on_delete=models.CASCADE, related_name="replies")
    answer = models.TextField(null=True)

    class Meta:
        db_table = "doctor_reply"

