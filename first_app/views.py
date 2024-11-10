from django.shortcuts import render,redirect
from . import models

def home(request):
    student = models.Student.objects.all()
    return render(request, 'first_app/home.html', {'data': student})

def delete_item(request, roll):
    std = models.Student.objects.get(pk=roll).delete()
    return redirect('homepage')