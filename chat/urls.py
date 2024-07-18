from django.urls import path

from .views import ChatView

urlpatterns = [
    path("<int:pk>", ChatView.as_view(), name="chat"),
    
]

