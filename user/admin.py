from django.contrib import admin
from .models import UserContactModel, UserModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links =['full_name']

    
@admin.register(UserContactModel)
class UserContactModelAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']
