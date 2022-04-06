from django import forms

from django.contrib.auth.models import User
from practitioner.models import Doctor
from .models import Patient,Appointment


class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:

        model=Patient

        fields=['address','mobile','status','symptoms','profile_pic']



class AppointmentForm(forms.ModelForm):

    doctorId=forms.ModelChoiceField(queryset= Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset= Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model= Appointment
        fields=['patientName','doctorName','appointmentDate','description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset= Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model= Appointment
        fields=['description','status']
