from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import  render, redirect
from management.forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from rest_framework.response import Response
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from django.views.generic import View

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
        

class RegisterApi(generics.GenericAPIView):
    """Register API"""

    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })