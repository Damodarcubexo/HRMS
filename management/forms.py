from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class SignUpForm(UserCreationForm):
	
    class Meta:
        model = User
        fields = ('first_name','last_name','email','contact','role','date_of_birth','gender','emp_image')
