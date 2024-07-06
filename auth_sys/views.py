from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, ListView

from .forms import MyUserCreationForm
from .models import MyUser

# Create your views here.

class CustomLoginView(LoginView):
    model = MyUser
    template_name = 'auth_sys/login.html'
    redirect_authenticated_user = True
    
class CustomLogoutView(LogoutView):
    ...
    
    
class CustomRegistrationView(CreateView):
    model = MyUser
    form_class = MyUserCreationForm
    template_name="auth_sys/register.html"
    success_url = reverse_lazy('login')
    
    

class UserListView(ListView):
    model = MyUser
    template_name = 'auth_sys/users-list.html'
    context_object_name = 'users'

        
    
   
