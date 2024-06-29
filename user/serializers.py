from user import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = [
            'telegram_id',
            'full_name',
            'phone',
            'email',
            'lang'
        ]

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserContactModel
        fields = [
            'full_name',
            'phone',
            'user',
        ]

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = models.UserModel
        fields = ['email', 'password']