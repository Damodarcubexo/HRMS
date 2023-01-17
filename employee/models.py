from django.db import models
from management.models import User

class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    GENDER = (('1','MALE'), ('2', 'FEMALE'),('3', 'OTHER'))
    email = models.EmailField(('email address'), unique=True)
    contact = models.IntegerField(null = False)
    date_of_birth = models.DateField(auto_now_add=False, null = True)
    gender = models.CharField(choices=GENDER, max_length=8)
    emp_image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.first_name

class Department(models.Model):
    department_name = models.CharField(max_length=50, null=False)

class PersonalDetail(models.Model):
    name = models.OneToOneField(User, on_delete= models.CASCADE, related_name='user_detail')
    personal_email = models.EmailField(max_length=50, blank= True)
    pan_card_number = models.CharField(max_length=30)
    aadhar_card_number = models.CharField(max_length=30)
    contact_number = models.IntegerField(null= True)
    emergency_contact_number = models.IntegerField(null= True)
    blood_group = models.CharField(max_length=5)
    Permanent_address = models.CharField(max_length=100)
    current_address= models.CharField(max_length=100)
    medical_condition = models.CharField(max_length=10, blank= True)
   
    def __str__(self):
        return self.name

class PastEmploymentDetail(models.Model):
    employee = models.OneToOneField(User, on_delete= models.CASCADE, related_name='user_employment_detail')
    company_name = models.CharField(max_length=50)
    role = models.CharField(max_length=40)
    date_of_joining = models.DateField(null= True)
    date_of_leaving = models.DateField(null= True)
    joining_letter = models.FileField(max_length=100)
    relieving_letter =   models.FileField(null=True, blank=True)
    payslips =  models.FileField(max_length=200)

class Leave(models.Model):
    STATUS = (('1','Pending'), ('2', 'Approved'), ('3', 'Declined'))
    type = (('sick','Sick'), ('inactive', 'Inactive'))
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    time_applied_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)
    reason = models.TextField(max_length=200)
    status = models.CharField(choices= STATUS, max_length= 10)

    @property
    def number_of_days(self):
        return (self.end_date - self.start_date).days

class Document(models.Model):               
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_upload = models.DateField(auto_now_add= True)
    pan_card = models.FileField(upload_to='media/uploads/')
    aadhar_card = models.FileField(upload_to='media/uploads/')
    marksheet_10th = models.FileField(upload_to='media/uploads/')
    marksheet_12th = models.FileField(upload_to='media/uploads/')
    ug = models.FileField(upload_to='media/uploads/')
    pg = models.FileField(upload_to='media/uploads/')

class EmployeeAttendance(models.Model):
    location_status = (('1','In office'), ('2', 'Apply for WFH'))
    attendance_status = (('1','Present'), ('2', 'Absent'))
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    time_in = models.TimeField(auto_now_add=True)
    time_out = models.TimeField(auto_now_add=True)
    break_duration = models.IntegerField()
    location = models.CharField(choices=location_status, max_length=20)
    status = models.CharField(choices=attendance_status, max_length=20)
    
class Event(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=100, blank = True)

    @property
    def number_of_days(self):
        return (self.end_date - self.start_date).days

class Holiday(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    occasion = models.CharField(max_length=50, required=True)

    @property
    def number_of_days(self):
        return (self.end_date - self.start_date).days

class Reimbursement(models.Model):
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    upload_receipt = models.FileField(upload_to='media/uploads/')
    bill_no = models.CharField(max_length=50, required= True)
    remark = models.TextField(max_length=100, blank= True)