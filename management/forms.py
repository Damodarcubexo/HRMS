from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Hr, Manager


class HrSignUpForm(UserCreationForm):
	
    class Meta:
        model = Hr
        fields = ('username','email','contact','date_of_birth','gender','emp_image')


class ManagerSignUpForm(UserCreationForm):
	
    class Meta:
        model = Manager
        fields = ('username','email','contact','date_of_birth','gender','emp_image')
