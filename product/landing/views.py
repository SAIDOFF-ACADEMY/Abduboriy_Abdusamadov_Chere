from product.landing import serializers
from product import models
from rest_framework import generics


# Product
class ProductView(generics.ListAPIView):
    queryset = models.ProductModel.objects.all()
    serializer_class = serializers.ProductSerializer
