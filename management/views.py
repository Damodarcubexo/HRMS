from django.shortcuts import render, HttpResponse
from django.shortcuts import  render, redirect
from management.forms import HrSignUpForm, ManagerSignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this


def hr_signup(request):
	if request.method == "POST":
		form = HrSignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponse('Hr Registered Successfully')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = HrSignUpForm()
	return render (request=request, template_name="employee/register.html", context={"form":form})

def manager_signup(request):
	if request.method == "POST":
		form = ManagerSignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponse('Manager Registered Successfully')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = ManagerSignUpForm()
	return render (request=request, template_name="employee/register.html", context={"form":form})
