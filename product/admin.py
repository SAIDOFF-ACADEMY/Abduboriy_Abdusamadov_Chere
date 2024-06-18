from django.contrib import admin
from .models import ProductModel, FreeProductModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(FreeProductModel)
class FreeProductModelAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']