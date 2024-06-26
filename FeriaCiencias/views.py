from django.shortcuts import render
from .models import Proyecto

def index(request):
    return render(request, "index.html")


def comopensar(request):
    proyecto = Proyecto.objects.get(nombre__icontains='inteligencia artificial')
    context = {"proyecto": proyecto}
    return render(request, "ia/comopensar.html", context)
