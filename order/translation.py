from .models import OrderModel
from modeltranslation.translator import TranslationOptions, register

@register(OrderModel)
class OrderModelTranslation(TranslationOptions):
    fields = ['status']