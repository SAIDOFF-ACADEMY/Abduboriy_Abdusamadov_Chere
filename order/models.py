from django.db import models
from product.models import ProductModel
from user.models import UserModel
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class OrderModel(BaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="orders")
    count = models.IntegerField()
    free_count = models.BigIntegerField()
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='customer')
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.TextField()
    status_changed_at = models.DateTimeField(auto_now_add=True)
    product_price = models.BigIntegerField()
    total_price = models.BigIntegerField()
    admin = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='admin')
    condition = models.CharField(max_length=255, choices=(
        (1, 'Qabul qilindi'), (2, 'Tayyorlanmoqda'), (3, 'Yo\'lda'), (4, 'Yetkazib berildi')))

    def __str__(self) -> str:
        return f"{self.id} {self.product.name}"

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
