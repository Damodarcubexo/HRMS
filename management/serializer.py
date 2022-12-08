from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from management.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','contact','role','date_of_birth',
        'gender','emp_image', 'password')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(first_name=validated_data['first_name'],  last_name=validated_data['last_name'], email = validated_data['email'],
        contact=validated_data['contact'], role=validated_data['role'], date_of_birth=validated_data['date_of_birth'],gender=validated_data['gender'],emp_image=validated_data['emp_image'], password = validated_data['password'])
        return user

# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'