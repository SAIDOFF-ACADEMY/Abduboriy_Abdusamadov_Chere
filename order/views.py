from rest_framework import generics
from order import serializers
from rest_framework import permissions
from order import models


class AdminOrderView(generics.ListAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializers
    permission_classes = [permissions.IsAdminUser]


class AdminOrderGetView(generics.RetrieveAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializers
    permission_classes = [permissions.IsAdminUser]


class AdminOrderUpdateView(generics.UpdateAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializers
    permission_classes = [permissions.IsAdminUser]


class AdminOrderDeleteView(generics.DestroyAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializers
    permission_classes = [permissions.IsAdminUser]


class AdminOrderCreateView(generics.CreateAPIView):
    queryset = models.OrderModel.objects.all()
    serializer_class = serializers.OrderSerializers
    permission_classes = [permissions.IsAdminUser]
