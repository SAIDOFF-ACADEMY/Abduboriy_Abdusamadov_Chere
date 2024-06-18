from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _


class ProductModel(models.Model):
    name = models.CharField(_("name"), max_length=255)
    content = RichTextField(_("content"))
    price = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

class FreeProductModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    count = models.IntegerField()
    free_count = models.IntegerField()

    def __str__(self) -> str:
        return self.product.name
    
    class Meta:
        verbose_name = 'freeProduct'
        verbose_name_plural = 'freeProducts'