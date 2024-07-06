from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="channels")
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following")
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("channel", kwargs={"pk": self.id})
    
    



class Post(models.Model):
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.content}"
    
    
    class Meta:
        abstract = True

class UserPost(Post):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")

class ChannelPost(Post):
    author = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="posts")
        
