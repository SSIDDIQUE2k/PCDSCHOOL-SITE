# main_app/views.py

from django.shortcuts import render

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
    """Calendar page view"""
    return render(request, 'educators.html')
