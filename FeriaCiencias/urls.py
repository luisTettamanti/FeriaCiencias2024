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
]