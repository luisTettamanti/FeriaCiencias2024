from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('ia/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('ia/seccion/<int:pk>/', views.seccion, name='seccion'),

    path('anarquiagin/proyectoanarquia/<int:pk>/', views.proyectoanarquia, name='proyectoanarquia'),
    path('anarquiagin/seccionanarquia/<int:pk>/', views.seccionanarquia, name='seccionanarquia'),
]