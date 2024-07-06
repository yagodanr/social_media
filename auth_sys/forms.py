from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "photo", )
        
class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUser
        fields = ('username', 'photo')
        widget = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "photo": forms.FileInput(attrs={"class": "form-control"})
        }
        

