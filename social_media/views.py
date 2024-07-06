from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, DetailView

from auth_sys.models import MyUser 
from .models import UserPost, ChannelPost, Channel


# Create your views here.
class MainPage(TemplateView):
    template_name = "social_media/main.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = dict()
        context["posts"] = list(UserPost.objects.all())
        context["posts"].extend(list(ChannelPost.objects.all()))
        context["posts"].sort(key=lambda x: x.created_at, reverse=True)
        # print(context)

        
        return context

class ChannelView(DetailView):
    model = Channel
    
class MyUserView(DetailView):
    model = MyUser
    template_name = "social_media/user_detail.html"
    context_object_name = "author"

