from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('ia/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('ia/seccion/<int:pk>/', views.seccion, name='seccion'),
    
    path('Cnaturales/proyecto/<int:pk>/', views.proyectoCnaturales, name='proyectoCnaturales'),
    path('Cnaturales/seccion/<int:pk>/', views.seccionCnaturales, name='seccionCnaturales'),
    path('Cnaturales/articulo/<int:pk>/', views.articuloCnaturales, name='articuloCnaturales'),
]