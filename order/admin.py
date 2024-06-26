from django.contrib import admin
from .models import OrderModel
from modeltranslation.admin import TranslationAdmin

class OrderAdmin(TranslationAdmin):
    list_display = ['status']
    readonly_fields = ['created_at', 'updated_at']
    
admin.site.register(OrderModel, OrderAdmin)
