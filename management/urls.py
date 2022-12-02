from django.urls import path, include
from management.views import signup, home_page,login_request

app_name = 'management'

urlpatterns = [
    path('', home_page, name = 'home_page'),
    path('login/', login_request, name = 'login'),
    path('signup/', signup, name = 'signup')
]