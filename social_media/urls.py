from django.urls import path

from .views import MainPage, ChannelView


urlpatterns = [
    path("", MainPage.as_view(), name="posts"),
    path("channel/<int:pk>", ChannelView.as_view(), name="channel"),
    
]

