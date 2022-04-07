from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [


    path('afterlogin', views.afterlogin_view, name='afterlogin'),


    path('adminclick', views.adminclick_view, name = 'adminclick'),
    path('doctorclick', views.doctorclick_view, name = 'doctorclick'),
    path('patientclick', views.patientclick_view, name = 'patientclick'),

    
    #: after a sucessful login, users are redirected 
    path('adminlogin', LoginView.as_view(template_name='accounts/adminlogin.html')),
    
    path('nologin', LoginView.as_view(template_name='accounts/adminlogin.html'), name='nologin'),
    path('doctorlogin', LoginView.as_view(template_name='accounts/doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='accounts/patientlogin.html')),


    path('logout', LogoutView.as_view(template_name='home/index.html'),name='logout'),

    
    path('patientsignup', views.patient_signup_view, name = 'patientsignup'),
    path('adminsignup', views.admin_signup_view, name = 'admin_signup'),
    path('adminlogin', LoginView.as_view(template_name='accounts/adminlogin.html'), name='adminlogin'),
    path('doctorlogin', LoginView.as_view(template_name='accounts/doctorlogin.html'), name='doctorlogin'),
    path('patientlogin', LoginView.as_view(template_name='accounts/patientlogin.html'), name='patientlogin'),
    path('logout', LogoutView.as_view(template_name='home/index.html'), name='logout'),

    #: dashboards
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('patient-dashboard', views.patient_dashboard_view, name='patient-dashboard'),
    path('doctor-dashboard', views.doctor_dashboard_view, name='doctor-dashboard'),
]
