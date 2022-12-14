from django.db import models

# Create your models here.

# python classes for database
class doctor(models.Model):
    First_name=models.CharField(max_length=20,null = True)
    Last_name=models.CharField(max_length=20,null = True)
    third_name=models.CharField(max_length=20, null=True)
    Address=models.CharField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    Birth_Date=models.DateField(null=True)
    Medical_Field=models.CharField(max_length=20,null=True)
    File_Diploma=models.FileField(null=True)
    class Meta:
        db_table = 'Doctor'

    
    
class patient(models.Model):
    First_name=models.CharField(max_length=20,null = True)
    Last_name=models.CharField(max_length=20,null = True)
    Phone_Number=models.CharField(max_length=10,null=True)
    Address=models.TextField(max_length=50,null=True)
    Email_Address=models.CharField(max_length=30,null=True)
    Birth_Date=models.DateField(null=True)
    class Meta:
        db_table = 'patient'

#     #password
#     def __str__(self):
#         return self.first_name
    
# class Admin(models.Model):
#     username="admin"
#     Password="adminadmin"