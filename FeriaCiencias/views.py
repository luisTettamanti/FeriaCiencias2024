from django.shortcuts import render
from .models import Proyecto, Seccion, Articulo, ArtImagen

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


def seccion(request, pk):
    proyectos = Proyecto.objects.all()
    secciones = Seccion.objects.all()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "ia/seccion.html", context)

def proyectoCnaturales(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "ciencias_naturales/proyectoCnaturales.html", context)


def seccionCnaturales(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(nombre__icontains="Ciencias Naturales")
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre).values()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo).values()
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos, "proyecto":proyecto}
    return render(request, "ciencias_naturales/seccionCnaturales.html", context)


def articuloCnaturales(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(nombre__icontains="Ciencias Naturales")
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre).values()
    articulo = Articulo.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion_id=articulo.idSeccion).values()
    seccion = Seccion.objects.filter(titulo=articulo.idSeccion).get()
    articuloImagen = ArtImagen.objects.get(idArticulo=pk)
    context = {"proyectos": proyectos, "secciones": secciones, "articulo": articulo, "articulos":articulos, "artImagen":articuloImagen, "proyecto":proyecto, "seccion": seccion}
    return render(request, "ciencias_naturales/articuloCnaturales.html", context)