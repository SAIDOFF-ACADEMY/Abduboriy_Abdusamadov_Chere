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
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')


class GalleryPhotoModel(BaseModel):
    photo = models.ImageField(upload_to=f"gallery/{year}/{month}/")


class SettingsModel(BaseModel):
    contact_telegram = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=13, null=True, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location_text = models.CharField(max_length=255)
    working_hours_start = models.TimeField()
    working_hours_end = models.TimeField()
    telegram_bot = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('setting')
        verbose_name_plural = _('settings')
