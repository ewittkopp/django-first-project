from django.urls import path
from first_app import views

urlpatterns = [
path('', views.index, name='index'),
path('employees/', views.emp_view, name='employees'),
path('about/', views.about, name='about'),
]