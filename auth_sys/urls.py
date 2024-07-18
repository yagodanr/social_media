from django.urls import path
from .views import CustomLoginView, CustomRegistrationView, CustomLogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegistrationView.as_view(), name='register')
    
]
