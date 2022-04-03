from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from patients.models import User


class UserRegisterForm(UserCreationForm) :
    email = forms.EmailField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    class Meta: 
        model = User    
        fields = ['username', 'firstname', 'lastname', 'email', 'password1', 'password2']