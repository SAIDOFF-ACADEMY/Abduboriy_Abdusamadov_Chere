from common import models
from rest_framework import serializers


class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PageModel
        fields = ['title', 'content']


class SettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SettingsModel
        fields = [
            'contact_telegram',
            'contact_phone',
            'longitude',
            'latitude',
            'location_text',
            'working_hours_start',
            'working_hours_end',
            'telegram_bot',
        ]


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.GalleryPhotoModel
        fields = ['photo']
