from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


from .models import Chat, Message

# Create your views here.
class ChatListView(TemplateView, LoginRequiredMixin):
    template_name = "chat/chats_list.html"

class ChatView(DetailView, LoginRequiredMixin):
    model = Chat
    template_name = "chat/chat_open.html"
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect("login")
        
        if "content" in request.POST:
            chat = self.get_object()
            
            msg = Message(sender=request.user, content=request.POST["content"], chat=chat)
            msg.save()
            
            
        
        return self.get(request, *args, **kwargs)


class ChatSearchView(TemplateView):
    template_name = "chat/chat_search.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if "search" in self.request.GET:
            context["chats"] = Chat.objects.filter(name__contains=self.request.GET["search"])
            
        return context
