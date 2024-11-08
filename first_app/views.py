from django.shortcuts import render
from . import models

def home(request):
    student = models.Student.objects.all()
    return render(request, 'first_app/home.html', {'data': student})
