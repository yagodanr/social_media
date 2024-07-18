from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chat

# Create your views here.

class ChatView(DetailView, LoginRequiredMixin):
    model = Chat
    template_name = "chat/chat_open.html"


class ChatListView(TemplateView, LoginRequiredMixin):
    model = Chat
    template_name = "chat/chats_list.html"