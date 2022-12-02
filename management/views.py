from django.shortcuts import render, HttpResponse
from django.shortcuts import  render, redirect
from management.forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.forms import AuthenticationForm

def home_page(request):
    return render(request, 'base.html')


def signup(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return HttpResponse('Registration Successful!')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignUpForm()
	return render (request=request, template_name="employee/register.html", context={"form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home_page")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="employee/login.html", context={"login_form":form})