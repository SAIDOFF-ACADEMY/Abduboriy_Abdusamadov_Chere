from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from main.models import BaseModel

class UserModel(AbstractUser, BaseModel):
    telegram_id = models.IntegerField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    lang = models.CharField(max_length=2, choices=[("uz", "Uzbek"), ("ru", "Russian")], default="uz")
    # username = None
    # last_name = None
    # first_name = None
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserContactModel(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="userContacts")

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = _('userContact')
        verbose_name_plural = _('usersContact')
