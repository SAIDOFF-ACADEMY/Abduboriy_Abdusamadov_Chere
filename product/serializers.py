from rest_framework import serializers
from product import models

class AdminProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = ['name', 'content', 'price']


class AdminFreeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FreeProductModel
        fields = ['product', 'count', 'free_count']