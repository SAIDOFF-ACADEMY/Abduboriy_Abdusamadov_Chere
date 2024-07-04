from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class UserModel(AbstractUser, BaseModel):
    telegram_id = models.IntegerField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    lang = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian")], default="uz")
    username = None
    last_name = None
    first_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.full_name or self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserContactModel(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="userContacts", null=True, blank=True)
    is_contacted = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = _('userContact')
        verbose_name_plural = _('usersContact')
