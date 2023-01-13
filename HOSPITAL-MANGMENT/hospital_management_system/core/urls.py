from django.urls import path
from .views import *
from . import views

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
    # path('patientList/',patientList.as_view(),name="patientList"), 
    # path('appointmentList/',appointmentList.as_view(),name="appointmentList"), 
    path('add_appointments/<int:p_id>',views.add_appointments, name='add_appointments'),
    # path('delete_appointment/<int:id>/<int:patient_id>/',delete_appointment,name="delete_appointment"),
    path('update_Appointment/<int:Appointment_pk>/<int:p_id>',update_Appointment,name="update_Appointment"),
    path('appointmentList/<int:patient_id>',appointmentList,name="appointmentList"),
    path('error_page/', views.error_page, name='error_page'),
    path('delete_appointment/<int:id>/<int:p_id>/',delete_appointment,name="delete_appointment"),
   path('send_summray/',send_summray, name='send_summray'),



]



