
from django.contrib import admin
from .models import Channel, UserPost, ChannelPost

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class UserPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_username', 'content', 'created_at', 'last_edit_at', )
    list_display_links = ('id', 'author_username', 'content')
    search_fields = ('id', 'author_username')
    
    def author_username(self, obj):
        return obj.author.username
    author_username.admin_order_field = 'author'  # Allows column order sorting
    author_username.short_description = 'Author Username'  # Renames column head

class ChannelPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'content', 'created_at', 'last_edit_at', )
    list_display_links = ('id', 'author_name', 'content')
    search_fields = ('id', 'author__name')
    
    def author_name(self, obj):
        return obj.author.name
    author_name.admin_order_field = 'author'  # Allows column order sorting
    author_name.short_description = 'Author Name'  # Renames column head

admin.site.register(Channel, ChannelAdmin)
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(ChannelPost, ChannelPostAdmin)
