from django.contrib import admin
from django.http import HttpRequest
from .models import GalleryPhotoModel, SettingsModel, PageModel
from modeltranslation.admin import TranslationAdmin


class PageAdmin(TranslationAdmin):
    list_display = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at', 'slug']


class SettingsAdmin(TranslationAdmin):
    list_display = ['location_text']
    readonly_fields = ['created_at', 'updated_at']

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None) -> bool:
        return False


admin.site.register(PageModel, PageAdmin)
admin.site.register(SettingsModel, SettingsAdmin)


@admin.register(GalleryPhotoModel)
class GalleryPhotoModel(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']
    readonly_fields = ['created_at', 'updated_at']
