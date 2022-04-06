from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('aboutus', views.aboutus_view, name = 'about'),
    path('contactus', views.contactus_view, name='contact'),
]