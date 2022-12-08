from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect
from management.forms import SignUpForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from management.models import User
from django.views.generic import View



def home_page(request):
    return render(request, 'base.html')


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('management:home_page')
    template_name = 'employee/register.html'


class LoginView(View):
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('home_page')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
        


#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })