from django.urls import path

from .views import MainPage, ChannelView, MyUserView


urlpatterns = [
    path("", MainPage.as_view(), name="main-page"),
    path("channel/<int:pk>", ChannelView.as_view(), name="channel"),
    path("user/<int:pk>", MyUserView.as_view(), name="user"),
    
]

