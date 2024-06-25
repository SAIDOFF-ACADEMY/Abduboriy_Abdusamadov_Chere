from django.contrib import admin
from .models import GalleryPhotoModel, SettingsModel, PageModel

@admin.register(GalleryPhotoModel)
class GalleryPhotoModel(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']

@admin.register(PageModel)
class PageModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register(SettingsModel)
class SettingsModelAdmin(admin.ModelAdmin):
    list_display = ['id']
    list_display_links = ['id']