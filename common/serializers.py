from common import models
from rest_framework import serializers


class AdminPageSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.PageModel
        fields = ['title', 'content']


class AdminSettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.SettingsModel
        fields = '__all__'


class AdminGallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.GalleryPhotoModel
        fields = ['photo']
