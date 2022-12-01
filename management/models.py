from django.db import models
from employee.models import User, Additional_Details

class Hr(User, Additional_Details):

    class Meta:
        db_table = "Hr"
        verbose_name = "Hr"
        verbose_name_plural = "Hr"

    def __str__(self):
        return self.first_name+self.last_name
        

class Manager(User, Additional_Details):
    
    class Meta:
        db_table = "Manager"
        verbose_name = "Manager"
        verbose_name_plural = "Manager"

    def __str__(self):
        return self.first_name+self.last_name
        
