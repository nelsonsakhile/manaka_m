from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClintsRegisterForm(forms.ModelForm):
    class Meta:
        model = ClintsRegister
        fields=[
            'number_of_clients',
            'Projects_completed',
            'successful_appeals',
        ]



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']