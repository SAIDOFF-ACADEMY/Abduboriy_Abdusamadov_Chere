from user import models
from rest_framework import generics
from user import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from django.utils.translation import gettext_lazy as _


class LoginView(generics.GenericAPIView):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.LoginSerializer
    permission_classes = [IsAdminUser]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid Credentials')}, status=status.HTTP_400_BAD_REQUEST)


class EmailView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        user = request.user
        if user:
            email = user.email
            return Response({'email': email}, status=status.HTTP_200_OK)
        return Response({'error': _("User does not exist")}, status=status.HTTP_400_BAD_REQUEST)
