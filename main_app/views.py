# main_app/views.py

from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import Teacher

# Define the home view function
def home(request):
    """Home page view"""
    return render(request, 'home.html')

def about(request):
    """About page view"""
    return render(request, 'about.html')

def services(request):
    """Services page view"""
    return render(request, 'services.html')

def educators(request):
    teachers = Teacher.objects.all()  # look familiar?
    return render(request, 'educators.html', {'teachers': teachers})

class TeacherCreate(CreateView):
    model = Teacher
    fields = "__all__"
