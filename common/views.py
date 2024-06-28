from common import models
from rest_framework import generics
from common import serializers
from rest_framework.response import Response


class GalleryView(generics.ListAPIView):
    queryset = models.GalleryPhotoModel.objects.all()
    serializer_class = serializers.GallerySerializers


class PageView(generics.ListAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.PageSerializers


class SettingsView(generics.GenericAPIView):
    queryset = models.SettingsModel.objects.all()
    serializer_class = serializers.SettingsSerializers

    def get(self, request, *args, **kwargs):
        setting = self.queryset.first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)
