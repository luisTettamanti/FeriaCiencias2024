from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('ia/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('ia/seccion/<int:pk>/', views.seccion, name='seccion'),
    path('impresion3d/proyecto3d/<int:pk>', views.proyecto3d, name='proyecto3d'),
    path('impresion3d/seccion3d/<int:pk>/', views.seccion3d, name='seccion3d'),
    
]