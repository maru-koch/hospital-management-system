from django.shortcuts import render
from django.views import generic
from .models import Patient,Practitioner,User


def index(request):
    return render(request,'patients/index.html')
    

class PatientRecordsView(generic.DetailView):
    pass

class BookAppointmentView(generic.CreateView):
    pass

# Create your views here.
