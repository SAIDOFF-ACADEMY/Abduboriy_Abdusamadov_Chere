from django.db import models
from product.models import ProductModel
from user.models import UserModel
from django.utils.translation import gettext_lazy as _

class OrderModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.IntegerField()
    free_count = models.BigIntegerField()
    customer = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    status = models.TextField(_("status"))
    status_changed_at = models.BigIntegerField()
    product_price = models.BigIntegerField()
    total_price = models.BigIntegerField()
    admin = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'
