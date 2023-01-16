from django.urls import path
from .views import *
from . import views
from django.urls import include, re_path


urlpatterns=[
    path('',index,name='index') ,
    path('signup-patient/',signup_patient,name="signup_patient"),
    path('Doctor_signup/',Doctor_signup,name="Doctor_signup"),
    path('login-patient/',login_patient,name="login_patient"),
    path('patient-homepag/',patient_homepage,name="patient_homepage"),
    path('login-Doctor/',login_Doctor,name="login_Doctor"),
    path('AdminLogin/',AdminLogin,name="AdminLogin"),
    path('admin_profile/',admin_profile,name="admin_profile"),
    path('doctor_profile/',doctor_profile,name="doctor_profile"), 
    path('patientList/',patientList.as_view(),name="patientList"), 
    path('doctorList/',doctorList.as_view(),name="doctorList"), 
    path('userslist/',userslist,name ='userslist'),
    path('update_patient/<int:patient_id>/', update_patient, name='update_patient'),
    path('update_doctor/<int:doctor_id>/', update_doctor, name='update_doctor'),
    path('doctor_detail/<int:DoctorID>/', doctorDetailView.as_view(), name='doctor_detail'),
    path('delete_doctor/<int:id>/',delete_doctor,name="delete_doctor"),
    path('delete_patient/<int:id>/',delete_patient,name="delete_patient"),
    path('search_doctor/',search_doctor,name="search_doctor"),
    path('logout_doctor/', logout_doctor, name='logout_doctor'),
    path('logout_doctor1/', help_logout_doctor, name='help_logout_doctor'),
    path('add_appointments/<int:p_id>',views.add_appointments, name='add_appointments'),
    path('update_Appointment/<int:Appointment_pk>/<int:p_id>',update_Appointment,name="update_Appointment"),
    path('appointmentList/<int:patient_id>',appointmentList,name="appointmentList"),
    path('error_page/', views.error_page, name='error_page'),
    path('delete_appointment/<int:id>/<int:p_id>/',delete_appointment,name="delete_appointment"),
    path('send_summray/',send_summray, name='send_summray'),
    path('summry_views/',summry_views.as_view(), name='summry_views'),
    path('summary/<int:patient_id>/', view_summary, name='view_summary'),
    path('patienttListinDoctor/',patienttListinDoctor, name='patienttListinDoctor'),
    path('test_blood_details/<int:test_number>/', test_blood_details.as_view(), name='test_blood_details'),
    path('test_blood/',test_blood.as_view(),name="test_blood"),
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
    path('logout_patient/', logout_patient, name='logout_patient'),
    path('logout_patient_accepted/', logout_patient_accepted, name='logout_patient_accepted'),
    path('receving_work/<str:doctor_name>/',receving_work,name="receving_work"),
    path('referrals_renewing/<instance_id>', referrals_renewing, name='referrals_renewing'),
    path('referral/<int:patient_id>/',referral,name="referral"),
    path('after_request_ref/<int:patient_id>/<int:refpk>/',after_request_ref,name="after_request_ref"),
    # path('renwe_ref/',renwe_ref.as_view(),name="renwe_ref"),
    path('renwe_ref/',renwe_ref,name="renwe_ref"),

    ]







