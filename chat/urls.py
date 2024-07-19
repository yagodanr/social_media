from django.urls import path

from .views import ChatView, ChatListView, ChatSearchView

urlpatterns = [
    path("<int:pk>", ChatView.as_view(), name="chat"),
    path("", ChatListView.as_view(), name="chats"),
    path("search/", ChatSearchView.as_view(), name="chat_search"),
    
]

