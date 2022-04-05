from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('patientsignup', views.patient_signup_view),
    path('adminlogin', LoginView.as_view(template_name='accounts/adminlogin.html'), name='adminlogin'),
    path('doctorlogin', LoginView.as_view(template_name='accounts/doctorlogin.html'), name='doctorlogin'),
    path('patientlogin', LoginView.as_view(template_name='accounts/patientlogin.html'), name='patientlogin'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='accounts/index.html'),name='logout'),
]