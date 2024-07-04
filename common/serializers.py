from django.utils.text import slugify
from django.db.models.signals import pre_save
from common import models
from rest_framework import serializers
from django.dispatch import receiver


class AdminPageCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = models.PageModel
        fields = ['title', 'content', 'slug']


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
