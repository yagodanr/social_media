from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chat

# Create your views here.

class ChatView(DetailView, LoginRequiredMixin):
    model = Chat
    template_name = "chat/chats.html"
