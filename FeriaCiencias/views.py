from django.shortcuts import render
from .models import Proyecto, Seccion, Articulo

def index(request):
    proyectos = Proyecto.objects.all()
    context = {"proyectos": proyectos}
    return render(request, "index.html", context)


def proyecto(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "ia/proyecto.html", context)
    
def proyectoanarquia(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "anarquiagin/proyectoanarquia.html", context)

def seccion(request, pk):
    proyectos = Proyecto.objects.all()
    secciones = Seccion.objects.all()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "ia/seccion.html", context)

def seccionanarquia(request, pk):
    proyectos = Proyecto.objects.all()
    secciones = Seccion.objects.all()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "anarquiagin/seccionanarquia.html", context)


