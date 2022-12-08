from django.urls import path, include
from management.views import RegisterApi, home_page,LoginView
from rest_framework_simplejwt import views as jwt_views

app_name = 'management'

urlpatterns = [
    path('', home_page, name = 'home_page'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('signup/', RegisterApi.as_view(), name = 'signup'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]