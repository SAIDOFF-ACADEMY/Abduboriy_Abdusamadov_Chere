from .models import UserModel, UserContactModel
from modeltranslation.translator import TranslationOptions, register

@register(UserModel)
class UserModelTranslation(TranslationOptions):
    fields = ['full_name']

@register(UserContactModel)
class UserContactModelTranslation(TranslationOptions):
    fields = ['full_name']
