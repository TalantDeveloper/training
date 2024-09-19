from django.shortcuts import render
from .function import create_qrcode
from .models import Direction, Student
from django.core.paginator import Paginator


def welcome(request):
    paginator = Paginator(Student.objects.all(), 5)
    students = paginator.page(1)
    context = {
        'students': students,
    }
    return render(request, 'main/welcome.html', context)


def students_view(request):
    students = Student.objects.all()
    paginator = Paginator(students, 10)


