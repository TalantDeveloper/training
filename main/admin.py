from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Direction)
class DirectionAdmin(TranslationAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Student)
class StudentAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'direction', 'study_start', 'study_end')
    list_display_links = ('id', 'full_name', 'direction', 'study_start', 'study_end')
    search_fields = ('id', 'full_name', 'direction', 'study_start', 'study_end')
    list_filter = ('direction', 'study_start', 'study_end')

