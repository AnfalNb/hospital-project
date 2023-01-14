from django.urls import path
from .views import *
from django.urls import include, re_path
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
    path('test_blood_details/<int:test_number>/', test_blood_details.as_view(), name='test_blood_details'),
    path('test_blood/',test_blood.as_view(),name="test_blood"),
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
    path('logout_patient/', logout_patient, name='logout_patient'),
    path('logout_patient_accepted/', logout_patient_accepted, name='logout_patient_accepted'),
    path('receving_work/<doctor_name>/',receving_work,name="receving_work"),
    path('referrals_renewing/<instance_id>', referrals_renewing, name='referrals_renewing'),
    path('referral/<int:patient_id>/',referral,name="referral"),
    path('after_request_ref/<int:patient_id>/',after_request_ref,name="after_request_ref"),
    path('renwe_ref/',renwe_ref.as_view(),name="renwe_ref"),


    



    
     ]







