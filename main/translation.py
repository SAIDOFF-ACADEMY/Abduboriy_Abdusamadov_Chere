from .models import SettingsModel, PageModel
from modeltranslation.translator import TranslationOptions, register

@register(PageModel)
class PageModelTranslation(TranslationOptions):
    fields = ['title', 'content']

@register(SettingsModel)
class SettingModelTranslation(TranslationOptions):
    fields = ['location_text']

