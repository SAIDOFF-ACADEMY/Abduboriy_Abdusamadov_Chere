from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class ProductModel(BaseModel):
    name = models.CharField(max_length=255)
    content = RichTextUploadingField()
    price = models.BigIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class FreeProductModel(BaseModel):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='freeProducts')
    count = models.IntegerField()
    free_count = models.IntegerField()

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name = _('freeProduct')
        verbose_name_plural = _('freeProducts')
