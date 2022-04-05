from django.urls import path
from .views import (
    PatientRecordsView, BookAppointmentView, index
)



app_name =  'patients'


urlpatterns = [
    path('',index,name='home'),
    path('<int:pk>/medical_records/',PatientRecordsView.as_view(), name='medical_records'),
    path('<int:pk>/book_appointment', BookAppointmentView.as_view(),name='book_appointment'),
]