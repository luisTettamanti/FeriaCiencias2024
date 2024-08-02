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
    seccion = Seccion.objects.get(id=pk)
    proyecto = Proyecto.objects.get(id=seccion.idProyecto_id)
    secciones = Seccion.objects.filter(idProyecto_id=proyecto.id)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "ia/seccion.html", context)


def proyecto3d(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "impresion3d/proyecto3d.html", context)


def seccion3d(request, pk):
    proyectos = Proyecto.objects.all()
    secciones = Seccion.objects.all()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    artimagen = ArtImagen.objects.all() #idArticulo__titulo__icontains=articulos.titulo
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos, "artimagen" : artimagen}
    return render(request, "impresion3d/seccion3d.html", context)    
    

def olimpiada(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)
    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "OIC/OIC.html", context)


def olimpiadaseccion(request, pk):
    proyectos = Proyecto.objects.all()
    secciones = Seccion.objects.all()
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)
    context = {"proyectos": proyectos, "secciones": secciones, "seccion": seccion, "articulos": articulos}
    return render(request, "OIC/OIA.html", context)


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


# Feria del Libro [Inicio]
def proyecto_fdl(request, pk):
    proyectos = Proyecto.objects.all()
    proyecto = Proyecto.objects.get(id=pk)
    secciones = Seccion.objects.filter(idProyecto__nombre__icontains=proyecto.nombre)

    context = {"proyecto": proyecto, "proyectos": proyectos, "secciones": secciones}
    return render(request, "FDL/proyectos.html", context)


def seccion_fdl(request, pk):
    proyectos = Proyecto.objects.all()
    
    seccion = Seccion.objects.get(id=pk)
    articulos = Articulo.objects.filter(idSeccion__titulo__icontains=seccion.titulo)

    seccion_filter = Seccion.objects.filter(idProyecto=seccion.idProyecto)


    id_art = None
    for x in articulos: id_art = x.id

    img = ArtImagen.objects.get(idArticulo=int(id_art))
    
    context = {"img":img,"proyectos": proyectos, "secciones": seccion_filter, "seccion": seccion, "articulos": articulos}
    return render(request, "FDL/seccion.html", context)
