from rest_framework import serializers
from user import models

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactModel
        fields = [
            'full_name',
            'phone',
            'user'
        ]