from django.db import models
from django.contrib.auth.models import AbstractUser
from management.manager import UserManager

class User(AbstractUser):

    username = None
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    email = models.EmailField(('email address'), unique=True)
    contact = models.CharField(max_length=12)
    date_of_birth = models.DateField(auto_now_add=False)
    gender = models.CharField(choices=GENDER, max_length=8)
    emp_image = models.ImageField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [username]

    objects = UserManager()

    def __str__(self):
        return self.email
