from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class PageModel(models.Model):
    slug = models.CharField(max_length=255)
    title = models.CharField(_("title"), max_length=255)
    content = RichTextField(_("content"))

    def __str__(self) -> str:
        return self.slug
    
    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'


class GalleryPhotoModel(models.Model):
    photo = models.ImageField(upload_to='gallery/')


class SettingsModel(models.Model):
    contact_telegram = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=13)
    logitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    location_text = models.CharField(_("location_text"), max_length=255)
    working_hours_start = models.BigIntegerField()
    working_hours_end = models.BigIntegerField()
    telegram_bot = models.CharField(max_length=255)


    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'