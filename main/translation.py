from .models import *
from modeltranslation.translator import TranslationOptions, register


@register(Direction)
class DirectionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Student)
class StudentTranslationOptions(TranslationOptions):
    fields = ('content',)
