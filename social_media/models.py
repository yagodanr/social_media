from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=255)
    
    members = models.ManyToManyField(User, related_name="channels")
    following = models.ManyToManyField(User, related_name="following")
    
    def __str__(self) -> str:
        return self.name
    



class Post(models.Model):
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.content}"
    
    
    class Meta:
        abstract = True

class UserPost(Post):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

class ChannelPost(Post):
    author = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="posts")
        
