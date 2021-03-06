from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField()
    appointmentTime = models.TimeField()
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)
    
    
class Record(models.Model):
    yes_no = [('n', 'No'), ('y', 'Yes')]
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    allergies = models.CharField(max_length = 200)
    operations = models.CharField(max_length = 100, choices = yes_no)
    no_of_operations = models.IntegerField()
    smoker = models.CharField(max_length = 100, choices = yes_no)
    drinker = models.CharField(max_length = 100, choices = yes_no)

    def __str__(self):
        return f"{self.patient.first_name} {self.patient.last_name}"
