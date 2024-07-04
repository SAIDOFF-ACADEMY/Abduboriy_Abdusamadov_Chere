from rest_framework import generics
from user.landing import serializers
from user import models

class UserContactView(generics.CreateAPIView):
    queryset = models.UserContactModel.objects.all()
    serializer_class = serializers.UserContactSerializer