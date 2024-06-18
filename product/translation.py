from .models import ProductModel
from modeltranslation.translator import TranslationOptions, register

@register(ProductModel)
class ProductModelTranslation(TranslationOptions):
    fields = ['name', 'content']