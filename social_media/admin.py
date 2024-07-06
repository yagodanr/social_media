from django.contrib import admin
from .models import Channel, UserPost, ChannelPost

class ChannelAdmin(admin.ModelAdmin):
    model = Channel
    list_display = ('id', 'name', 'admin_photo')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

    fieldsets = (
        (None, {"fields": ('name', 'description', ('admin_photo', 'photo'), 'members', 'following')}),
    )
    readonly_fields = ['admin_photo']


class UserPostAdmin(admin.ModelAdmin):
    model = UserPost
    list_display = ('id', 'admin_photo', 'content', 'created_at', 'last_edit_at', )
    list_display_links = ('id', 'content')
    search_fields = ('id',)

    fieldsets = (
        (None, {"fields": ('content', 'created_at',  ('admin_photo', 'photo'))}),
    )
    readonly_fields = ['admin_photo', 'created_at']
    
    

class ChannelPostAdmin(admin.ModelAdmin):
    model = ChannelPost
    list_display = ('id', 'admin_photo', 'content', 'created_at', 'last_edit_at', )
    list_display_links = ('id', 'content')
    search_fields = ('id', )

    fieldsets = (
        (None, {"fields": ('content', 'created_at',  ('admin_photo', 'photo'))}),
    )
    readonly_fields = ['admin_photo', 'created_at']
    
    

admin.site.register(Channel, ChannelAdmin)
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(ChannelPost, ChannelPostAdmin)
