from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('ia/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('ia/seccion/<int:pk>/', views.seccion, name='seccion'),
    path('Historia/historiaCba/<int:pk>', views.proyectoHistoria, name='proyectoHistoria'),
    path('Historia/seccionCba/<int:pk>/', views.seccionHistoria, name='seccionHistoria'),
    path('Historia/articuloCba/<int:pk>/', views.articuloHistoria, name='articuloHistoria'),
]