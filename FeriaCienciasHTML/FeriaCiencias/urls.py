from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('html/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('html/seccion/<int:pk>/', views.seccion, name='seccion'),
]