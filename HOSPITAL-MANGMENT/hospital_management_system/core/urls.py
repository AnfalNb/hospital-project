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
    path('update-patient/<str:pk>p',update_patient,name="update_patient"), 
    path('patientList/',patientList.as_view(),name="patientList"), 
    path('logout_admin/',logout_admin, name="logout_admin"), #admin logout
    # path('sendupdatestoadmin/',sendupdatestoadmin,name="sendupdatestoadmin"),#doctor updates orzalena
    path('askDoctor/', AskDoctor, name="ask_doctor"),
    # path('answerUrPatient/', AnswerUrPatient, name="AnswerUrPatient"),
    path("reply_patients/", reply_patients, name="reply_patients"),
    path("reply_patient/<int:pk>/", reply_patient, name="reply_patient"),
    path("patient_messages/", patient_messages, name="patient_messages"),
    path("shift_updates/", shift_updates, name="shift_updates"),      
         path("admin_shift_updates/", admin_shift_updates, name="admin_shift_updates"), 
]