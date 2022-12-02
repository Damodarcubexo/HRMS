from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction

class SignUpForm(UserCreationForm):
	
    class Meta:
        model = User
        fields = ('first_name','last_name','email','contact','role','date_of_birth','gender','emp_image')
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_active = True

        if user.role == 'hr':
            user.save()
            return user
        elif user.role == 'manager':
            user.save()
            return user
        else:
            pass

# class ManagerSignUpForm(UserCreationForm):
	
#     class Meta:
#         model = User
#         fields = ('email','contact','role','date_of_birth','gender','emp_image')
        
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_active = True
#         user.role = 'manager'
#         user.save()
#         return user