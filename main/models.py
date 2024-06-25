from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
import datetime

year = datetime.datetime.now().year
month = datetime.datetime.now().month

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class PageModel(BaseModel):
    slug = models.SlugField()
    title = models.CharField(_("title"), max_length=255)
    content = RichTextUploadingField(_("content"))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')


class GalleryPhotoModel(BaseModel):
    photo = models.ImageField(upload_to=f"gallery/{year}/{month}/")


class SettingsModel(models.Model):
    contact_telegram = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=13)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location_text = models.CharField(_("location_text"), max_length=255)
    working_hours_start = models.SmallIntegerField()
    working_hours_end = models.SmallIntegerField()
    telegram_bot = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('setting')
        verbose_name_plural = _('settings')
