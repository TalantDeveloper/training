from django.shortcuts import render
from .function import create_qrcode


def welcome(request):
    image = create_qrcode(request)
    return render(request, 'main/welcome.html', {'image': image})

