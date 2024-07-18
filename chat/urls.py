from django.urls import path

from .views import ChatView, ChatListView

urlpatterns = [
    path("<int:pk>", ChatView.as_view(), name="chat"),
    path("", ChatListView.as_view(), name="chats"),
    
]

