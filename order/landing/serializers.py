from order import models
from rest_framework import serializers


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OrderModel
        fields = [
            'product',
            'count',
            'free_count',
            'customer',
            'longitude',
            'latitude',
            'status',
            'status_changed_at',
            'product_price',
            'total_price',
            'admin',
            'condition'
        ]


class OrderCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OrderModel
        fields = [
            'product',
            'count',
            'free_count',
            'customer',
            'longitude',
            'latitude',
            'status',
            'status_changed_at',
            'product_price',
            'total_price',
            'admin',
            'condition'
        ]
