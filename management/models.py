from django.db import models
from django.contrib.auth.models import AbstractUser
from management.manager import UserManager


# class Hr(User, Additional_Details):

#     class Meta:
#         db_table = "Hr"
#         verbose_name = "Hr"
#         verbose_name_plural = "Hr"

#     def __str__(self):
#         return self.first_name+self.last_name
        

# class Manager(User, Additional_Details):
    
#     class Meta:
#         db_table = "Manager"
#         verbose_name = "Manager"
#         verbose_name_plural = "Manager"

#     def __str__(self):
#         return self.first_name+self.last_name
        
class User(AbstractUser):
    username = None
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    ROLES = (('hr', 'Hr'), ('manager', 'Manager'))
    role = models.CharField( max_length=20,choices=ROLES,default='hr')
    email = models.EmailField(('email address'), unique=True)
    contact = models.IntegerField(null = True)
    date_of_birth = models.DateField(auto_now_add=False, null = True)
    gender = models.CharField(choices=GENDER, max_length=8)
    emp_image = models.ImageField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email