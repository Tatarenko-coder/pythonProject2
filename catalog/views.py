from django.shortcuts import render
from .models import Project

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})


def contact(request):
    return render(request, 'contact.html')

