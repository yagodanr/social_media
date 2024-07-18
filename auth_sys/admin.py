from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import MyUser


class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ('id', 'username', 'description', "email", "is_staff", "is_active", 'admin_photo')
    list_display_links = ('id', 'username')
    list_filter = ('id', 'username', "email", "is_staff", "is_active",)
    
    fieldsets = (
        (None, {"fields": ("username", "email", "password", ('admin_photo', 'photo'))}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    readonly_fields = ['admin_photo']
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "description", "password1", "password2", "photo", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ('id', "username",)
    ordering = ("id",)


admin.site.register(MyUser, MyUserAdmin)

