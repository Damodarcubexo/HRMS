from django.urls import path, include
from management.views import hr_signup, manager_signup

app_name = 'management'

urlpatterns = [

    path('signup/hr/', hr_signup, name = 'hr_signup'),
    path('signup/manager/', manager_signup, name = 'manager_signup')

]