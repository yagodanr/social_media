from django.urls import path

from .views import ChatView, ChatListView, ChatSearchView, ChatFollowView

urlpatterns = [
    path("<int:pk>", ChatView.as_view(), name="chat"),
    path("", ChatListView.as_view(), name="chats"),
    path("search/", ChatSearchView.as_view(), name="chat_search"),
    path("follow/<int:pk>", ChatFollowView.as_view(), name="chat_follow"),
    
]

