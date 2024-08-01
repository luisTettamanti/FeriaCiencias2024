from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=100)
    link = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.nombre


class Seccion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=100)
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)
    link = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.titulo


class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    idSeccion = models.ForeignKey(Seccion, on_delete=models.PROTECT)
    link = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.titulo


class ArtImagen(models.Model):
    imagen = models.CharField(max_length=100)
    idArticulo = models.ForeignKey(Articulo, related_name='imagenes', on_delete=models.PROTECT)

    def __str__(self):
        return self.imagen