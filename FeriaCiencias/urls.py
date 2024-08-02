from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),

    path('ia/proyecto/<int:pk>', views.proyecto, name='proyecto'),
    path('ia/seccion/<int:pk>/', views.seccion, name='seccion'),

    path('olimpiada/proyecto/<int:pk>', views.olimpiada, name='olimpiada'),
    path('olimpiada/seccion/<int:pk>/', views.olimpiadaseccion, name='olimpiadaseccion'),
    
    path('Cnaturales/proyecto/<int:pk>/', views.proyectoCnaturales, name='proyectoCnaturales'),
    path('Cnaturales/seccion/<int:pk>/', views.seccionCnaturales, name='seccionCnaturales'),
    path('Cnaturales/articulo/<int:pk>/', views.articuloCnaturales, name='articuloCnaturales'),

    path('impresion3d/proyecto3d/<int:pk>', views.proyecto3d, name='proyecto3d'),
    path('impresion3d/seccion3d/<int:pk>/', views.seccion3d, name='seccion3d'),

    path('FDL/proyectos/<int:pk>', views.proyecto_fdl, name='proyecto'),
    path('FDL/seccion/<int:pk>/', views.seccion_fdl, name='seccion'),
]