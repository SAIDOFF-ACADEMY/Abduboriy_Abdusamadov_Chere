from django.contrib import admin
from .models import UserContactModel, UserModel
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ['full_name', 'email']
    list_display_links =['full_name', 'email']
    search_fields = ("email", "full_name")
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("full_name", "phone", "lang")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    
@admin.register(UserContactModel)
class UserContactModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
