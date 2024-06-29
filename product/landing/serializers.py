from product import models
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductModel
        fields = ['name', 'content', 'price']


# class FreeProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.ProductModel
#         fields = ['product', 'count', 'free_count']
