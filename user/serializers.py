from user import models
from rest_framework import serializers

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = [
            'telegram_id',
            'full_name',
            'phone',
            'email',
            'lang'
        ]

class AdminUserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactModel
        fields = [
            'full_name',
            'phone',
            'user',
        ]

class AdminLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = models.UserModel
        fields = ['email', 'password']