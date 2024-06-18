from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class UserModel(AbstractUser):
    telegram_id = models.BigIntegerField()
    full_name = models.CharField(_("full_name"), max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class UserContactModel(models.Model):
    full_name = models.CharField(_("full_name"), max_length=255)
    phone = models.CharField(max_length=255)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'userContact'
        verbose_name_plural = 'usersContact'
        