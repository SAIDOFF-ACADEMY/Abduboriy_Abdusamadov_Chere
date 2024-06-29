from django.shortcuts import render
from product import models
from product import serializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# Product
class ProductView(generics.ListAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.AdminProductSerializer
    permission_classes = [IsAdminUser]


class ProductGetView(generics.RetrieveAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.AdminProductSerializer
    permission_classes = [IsAdminUser]


class ProductCreateView(generics.CreateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.AdminProductSerializer
    permission_classes = [IsAdminUser]


class ProductDeleteView(generics.DestroyAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.AdminProductSerializer
    permission_classes = [IsAdminUser]


class ProductUpdateView(generics.UpdateAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.AdminProductSerializer
    permission_classes = [IsAdminUser]


# FreeProduct
class FreeProductView(generics.ListAPIView):
    queryset = models.FreeProductModel.objects.all()
    serializer_class = serializers.AdminFreeProductSerializer
    permission_classes = [IsAdminUser]


class FreeProductGetView(generics.RetrieveAPIView):
    queryset = models.FreeProductModel.objects.all()
    serializer_class = serializers.AdminFreeProductSerializer
    permission_classes = [IsAdminUser]


class FreeProductCreateView(generics.CreateAPIView):
    queryset = models.FreeProductModel.objects.all()
    serializer_class = serializers.AdminFreeProductSerializer
    permission_classes = [IsAdminUser]


class FreeProductDeleteView(generics.DestroyAPIView):
    queryset = models.FreeProductModel.objects.all()
    serializer_class = serializers.AdminFreeProductSerializer
    permission_classes = [IsAdminUser]


class FreeProductUpdateView(generics.UpdateAPIView):
    queryset = models.FreeProductModel.objects.all()
    serializer_class = serializers.AdminFreeProductSerializer
    permission_classes = [IsAdminUser]
