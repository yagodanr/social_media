from django.db import models
from django.conf import settings


# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="chats")

    def __str__(self) -> str:
        if self.name is None:
            return self.members
        
        return self.name
    

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    content = models.CharField(max_length=511)
    
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.sender}:  {self.content}"
    
    class Meta:
        ordering = ["-created_at"]