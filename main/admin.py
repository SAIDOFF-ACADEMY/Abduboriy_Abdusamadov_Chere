from django.contrib import admin
from .models import GalleryPhotoModel, SettingsModel, PageModel
from modeltranslation.admin import TranslationAdmin

class PageAdmin(TranslationAdmin):
    list_display = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']

class SettingsAdmin(TranslationAdmin):
    list_display = ['location_text']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(PageModel, PageAdmin)
admin.site.register(SettingsModel, SettingsAdmin)



@admin.register(GalleryPhotoModel)
class GalleryPhotoModel(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    readonly_fields = ['created_at', 'updated_at']