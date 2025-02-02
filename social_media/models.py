from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.safestring import mark_safe

# Create your models here.
class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    photo = models.ImageField(upload_to="channel/%Y/%m/%d/", blank=True, null=True)
    def admin_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width=100>')
    admin_photo.short_description = 'Photo'
    admin_photo.allow_tags = True
    
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="channels")
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="following")
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("channel", kwargs={"pk": self.id})
    
    



class Post(models.Model):
    content = models.TextField()
    photo = models.ImageField(upload_to="post/%Y/%m/%d/", blank=True, null=True)
    def admin_photo(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" width=100>')
    admin_photo.short_description = 'Photo'
    admin_photo.allow_tags = True
    
    created_at = models.DateTimeField(auto_now_add=True)
    last_edit_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id} : {self.content}"
    
    
    class Meta:
        abstract = True
        ordering = ["-created_at"]

class UserPost(Post):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")

class ChannelPost(Post):
    author = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="posts")
        
