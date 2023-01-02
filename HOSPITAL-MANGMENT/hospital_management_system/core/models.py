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






















class WorkSchedule(models.Model):
    calendar_id=models.AutoField(primary_key=True)
    name_doc=models.CharField(max_length=225)
    owner=models.ForeignKey(doctor_a, on_delete=models.CASCADE)
    visible_for=models.ManyToManyField(doctor_a,related_name="visible_for")
    editable_by=models.ManyToManyField(doctor_a,related_name="editable_by")

    def __str__(self):
        return self.name_doc

class Event(models.Model):
   
    event_id=models.AutoField(primary_key=True)
    calendar_id=models.ForeignKey(WorkSchedule, on_delete=models.CASCADE)
    name_ev=models.CharField(max_length=225)
    start_date=models.DateField()
    end_date=models.DateField(null=True,blank=True)
    event_type=models.CharField(max_length=2)
    def __str__(self):
        return self.name_ev

