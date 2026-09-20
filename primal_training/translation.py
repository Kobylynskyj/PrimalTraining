from modeltranslation.translator import register, TranslationOptions
from .models import FitnessClass

@register(FitnessClass)
class FitnessClassTranslationOptions(TranslationOptions):
    fields = ('title', 'description')