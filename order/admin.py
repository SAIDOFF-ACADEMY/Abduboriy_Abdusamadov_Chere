from django.contrib import admin
from .models import OrderModel

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']