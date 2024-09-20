from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('students/', students_view, name='students'),
    path('students/<int:student_id>/', student_view, name='student'),
]
