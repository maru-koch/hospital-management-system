from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.db.models import Q
from .forms import PatientForm

def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

# Create your views here.
def patientclick_view(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect('afterlogin')
    return render(request,'patient/patientclick.html')


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')

def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.assignedDoctorId=request.POST.get('assignedDoctorId')
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'hospital/patientsignup.html',context=mydict)

#----------------------------------------------------------------------------------
#------------------------ PATIENT RELATED VIEWS START -----------------------------
#----------------------------------------------------------------------------------

@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_dashboard_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id)
    doctor=models.Doctor.objects.get(user_id=patient.assignedDoctorId)
    mydict={
    'patient':patient,
    'doctorName':doctor.get_name,
    'doctorMobile':doctor.mobile,
    'doctorAddress':doctor.address,
    'symptoms':patient.symptoms,
    'doctorDepartment':doctor.department,
    'admitDate':patient.admitDate,
    }
    return render(request,'hospital/patient_dashboard.html',context=mydict)



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
def patient_appointment_view(request):
    # patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'patient/patient_appointment.html')



# @login_required(login_url='patientlogin')
# @user_passes_test(is_patient)
def patient_book_appointment_view(request):
    form = PatientForm(request.POST)
    # # patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    # # message=None
    # mydict={'appointmentForm':form,'patient':patient,'message':message}
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('patient-view-appointment')

    return render(request,'patient/patient_book_appointment.html', {'form':form})



def patient_view_doctor_view(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    return render(request,'patient/patient_view_doctor.html',{'patient':patient,'doctors':doctors})



def search_doctor_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    
    # whatever user write in search box we get in query
    query = request.GET['query']
    doctors=models.Doctor.objects.all().filter(status=True).filter(Q(department__icontains=query)| Q(user__first_name__icontains=query))
    return render(request,'patient/patient_view_doctor.html',{'patient':patient,'doctors':doctors})




@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_view_appointment_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    appointments=models.Appointment.objects.all().filter(patientId=request.user.id)
    return render(request,'patient/patient_view_appointment.html',{'appointments':appointments,'patient':patient})



@login_required(login_url='patientlogin')
@user_passes_test(is_patient)
def patient_discharge_view(request):
    patient=models.Patient.objects.get(user_id=request.user.id) #for profile picture of patient in sidebar
    dischargeDetails=models.PatientDischargeDetails.objects.all().filter(patientId=patient.id).order_by('-id')[:1]
    patientDict=None
    if dischargeDetails:
        patientDict ={
        'is_discharged':True,
        'patient':patient,
        'patientId':patient.id,
        'patientName':patient.get_name,
        'assignedDoctorName':dischargeDetails[0].assignedDoctorName,
        'address':patient.address,
        'mobile':patient.mobile,
        'symptoms':patient.symptoms,
        'admitDate':patient.admitDate,
        'releaseDate':dischargeDetails[0].releaseDate,
        'daySpent':dischargeDetails[0].daySpent,
        'medicineCost':dischargeDetails[0].medicineCost,
        'roomCharge':dischargeDetails[0].roomCharge,
        'doctorFee':dischargeDetails[0].doctorFee,
        'OtherCharge':dischargeDetails[0].OtherCharge,
        'total':dischargeDetails[0].total,
        }
        print(patientDict)
    else:
        patientDict={
            'is_discharged':False,
            'patient':patient,
            'patientId':request.user.id,
        }
    return render(request,'patient/patient_discharge.html',context=patientDict)


def medical_record(request):
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            allergies = form.cleaned_data['allergies']
            operations = form.cleaned_data['operations']
            no_of_operations = form.cleaned_data['no_of_operations']
            smoker = form.cleaned_data['smoker']
            drinker = form.cleaned_data['drinker']
            
            medical_record = Record.objects.create(
                
                allergies = allergies,
                operations = operations,
                no_of_operations = no_of_operations,
                smoker = smoker,
                drinker = drinker,
            )
            medical_record.save()
            
            return redirect('is_filled')
        
        else:
            form = MedicalRecordForm()

        return render(request, 'is_filled.html', {'form': form})
        
        
def is_filled(request):
    return render(request, 'patient/is_filled.html')


#------------------------ PATIENT RELATED VIEWS END ------------------------------
#---------------------------------------------------------------------------------
