from django.db import models
from django.contrib.auth.models import AbstractUser
from management.manager import UserManager

class Additional_Details(models.Model):
    STATUS = (('active','Active'), ('inactive', 'Inactive'))
    ACCESS = (('true','TRUE'), ('false', 'FALSE'))
    employee_Id = models.CharField(max_length=12)
    joining_date = models.DateField(null= True)
    position = models.CharField(max_length=20)
    status = models.CharField(choices=STATUS, max_length=20, )
    access: models.CharField(choices=ACCESS, max_length=10)
    member_of = models.CharField(max_length=20)
    guardian_name = models.CharField(max_length=20)
    alternate_contact = models.IntegerField(null= True)
    religion = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    Permanent_address = models.CharField(max_length=100)
    current_address= models.CharField(max_length=100)
    remark =   models.CharField(max_length=20)
    description =  models.CharField(max_length=200)
    previous_organisation = models.CharField(max_length=30)
    previous_position = models.CharField(max_length=40)
    previous_salary = models.CharField(max_length=10)
    previous_joining_letter = models.CharField(max_length=100)
    relieving_letter =   models.ImageField(null=True, blank=True)
    reason_of_relieving =  models.CharField(max_length=200)
    
    class Meta:
        abstract = True


class User(AbstractUser):
    username = models.CharField(max_length=20, null= True)
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    email = models.EmailField(('email address'), unique=True)
    contact = models.IntegerField(null = True)
    date_of_birth = models.DateField(auto_now_add=False, null = True)
    gender = models.CharField(choices=GENDER, max_length=8)
    emp_image = models.ImageField(blank=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        abstract = False


    def __str__(self):
        return self.email


class Employee(User, Additional_Details):
    class Meta:
        db_table = "Employee"
        verbose_name = "Employee"
        verbose_name_plural = "Employee"

    def __str__(self):
        return self.first_name+self.last_name
        
