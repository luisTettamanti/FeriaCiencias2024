from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Seccion(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.CharField(max_length=50)
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    idSeccion = models.ForeignKey(Seccion, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class ArtImagen(models.Model):
    imagen = models.CharField(max_length=50)
    idArticulo = models.ForeignKey(Articulo, on_delete=models.PROTECT)

    def __str__(self):
        return self.imagen