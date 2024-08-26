from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('educators/', views.educators, name='educators'),
    path('teachers-create/', views.TeacherCreate.as_view(), name='teachers-create'),


]