from django.contrib import admin

from .models import Chat, Message

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'content', 'chat', 'created_at', 'last_edit_at', )
    list_display_links = ('id', 'content')
    
    

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)