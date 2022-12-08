from django.db import models
from management.models import User
from django.urls import reverse

class AdditionalDetail(models.Model):
    STATUS = (('active','Active'), ('inactive', 'Inactive'))
    ACCESS = (('true','TRUE'), ('false', 'FALSE'))
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name='user_detail')
    employee_Id = models.CharField(max_length=12)
    joining_date = models.DateField(null= True)
    position = models.CharField(max_length=20)
    status = models.CharField(choices=STATUS, max_length=20)
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
    
    def __str__(self):
        return self.user
    


class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    email = models.EmailField(('email address'), unique=True)
    contact = models.IntegerField(null = False)
    date_of_birth = models.DateField(auto_now_add=False, null = True)
    gender = models.CharField(choices=GENDER, max_length=8)
    emp_image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.first_name
        
    # def get_absolute_url(self):
    #     return reverse("hrms:employee_view", kwargs={"pk": self.pk})
