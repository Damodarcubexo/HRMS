from django.db import models
from django.contrib.auth.models import AbstractUser
from management.manager import UserManager
       
class User(AbstractUser):
    username = None
    GENDER = (('1','Male'), ('2', 'Female'),('3', 'Other'))
    ROLES = (('1', 'Hr admin'), ('2', 'Employee'))
    STATUS = (('1', 'Active'), ('2', 'Pending'), ('3', 'Inactive'))
    role = models.CharField( max_length=20, choices = ROLES, default='1')
    email = models.EmailField(('email address'), unique=True)
    contact = models.IntegerField(null = True)
    status = models.CharField(choices=STATUS, default= '2')
    date_of_birth = models.DateField(auto_now_add=False, null = True)
    gender = models.CharField(choices=GENDER, max_length=8)
    image = models.ImageField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
