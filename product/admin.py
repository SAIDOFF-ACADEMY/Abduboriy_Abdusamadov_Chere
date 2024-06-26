from django.contrib import admin
from .models import ProductModel, FreeProductModel
from modeltranslation.admin import TranslationAdmin

class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'content', 'price')
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(ProductModel, ProductAdmin)

@admin.register(FreeProductModel)
class FreeProductModelAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    readonly_fields = ['created_at', 'updated_at']
