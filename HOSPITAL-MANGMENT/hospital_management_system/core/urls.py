from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index') ,
    # path('patient_signup/',patient_signup),
    # path('login_Doctor/',login_Doctor),
    # path('signup_Doctor/',signup_Doctor),
    # path('login_patient/',login_patient,name="login_patient"),
    # path('AdminLogin/',AdminLogin,name="AdminLogin"),
    # path('AskDoctor/',AskDoctor,name="AskDoctor"),

    path('signup-patient/',signup_patient,name="signup_patient"),
    path('Doctor_signup/',Doctor_signup,name="Doctor_signup"),
    path('login-patient/',login_patient,name="login_patient"),
    path('patient-homepag/',patient_homepage,name="patient_homepage"),
    path('login-Doctor/',login_Doctor,name="login_Doctor"),
    path('AdminLogin/',AdminLogin,name="AdminLogin"),
    path('admin_profile/',admin_profile,name="admin_profile"),
    path('doctor_profile/',doctor_profile,name="doctor_profile"), 
    # path('update-patient/<str:pk>p',update_patient,name="update_patient"), 
    path('patientList/',patientList.as_view(),name="patientList"), 
    path('doctorList/',doctorList.as_view(),name="doctorList"), 
    path('userslist/',userslist,name ='userslist'),
    path('update_patient/<int:patient_id>/', update_patient, name='update_patient'),
    path('update_doctor/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('doctor_detail/<int:DoctorID>/', doctorDetailView.as_view(), name='doctor_detail'),
    path('delete_doctor/<int:id>/',delete_doctor,name="delete_doctor"),
    
    ]







