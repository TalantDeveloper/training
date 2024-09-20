from django.shortcuts import render, redirect
from .function import create_qrcode
from .models import Direction, Student
from django.core.paginator import Paginator


def welcome(request):
    paginator = Paginator(Student.objects.all().order_by('-create_at'), 5)
    students = paginator.page(1)
    context = {
        'students': students,
    }
    return render(request, 'main/welcome.html', context)


def students_view(request):
    students = Student.objects.all().order_by('-create_at')
    paginator = Paginator(students, 10)
    if request.GET.get('page'):
        page_number = int(request.GET.get('page'))
    else:
        page_number = 1
    students = paginator.page(page_number)
    context = {'students': students, 'page_number': page_number}
    return render(request, 'main/students.html', context)


def student_view(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
        image = create_qrcode(request, student_id)
    except Student.DoesNotExist:
        return redirect('main:welcome')
    paginator = Paginator(Student.objects.all().order_by('-create_at'), 5)
    students = paginator.page(1)
    context = {
        'student': student,
        'students': students,
        'image': image,
    }
    return render(request, 'main/student.html', context)
