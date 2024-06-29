from common import models
from rest_framework import generics
from common import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser


# Gallery
class GalleryView(generics.ListAPIView):
    queryset = models.GalleryPhotoModel.objects.all()
    serializer_class = serializers.AdminGallerySerializers
    permission_classes = [IsAdminUser]


class GalleryDeleteView(generics.DestroyAPIView):
    queryset = models.GalleryPhotoModel.objects.all()
    serializer_class = serializers.AdminGallerySerializers
    permission_classes = [IsAdminUser]


class GalleryCreateView(generics.CreateAPIView):
    queryset = models.GalleryPhotoModel.objects.all()
    serializer_class = serializers.AdminGallerySerializers
    permission_classes = [IsAdminUser]


# Page
class PageView(generics.ListAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.AdminPageSerializers
    permission_classes = [IsAdminUser]


class PageCreateView(generics.CreateAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.AdminPageSerializers
    permission_classes = [IsAdminUser]


class PageUpdateView(generics.UpdateAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.AdminPageSerializers
    permission_classes = [IsAdminUser]


class PageDeleteView(generics.DestroyAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.AdminPageSerializers
    permission_classes = [IsAdminUser]


class PageGetView(generics.RetrieveAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.AdminPageSerializers
    permission_classes = [IsAdminUser]


# Setting
class SettingsView(generics.GenericAPIView):
    queryset = models.SettingsModel.objects.all()
    serializer_class = serializers.AdminSettingsSerializers
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
