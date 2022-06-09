from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Accesorio



# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")

def calculadora(request):
    return render(request, "calculadora.html")

def Contacto(request):
    return render(request, "Contacto.html")

def Feriados(request):
    return render(request, "Feriados.html")

def galeria(request):
    return render(request, "galeria.html")

def registracion(request):
    return render(request, "registracion.html")

def somos(request):
    return render(request, "somos.html")

def mostrar(request):
    accesorios = Accesorio.objects.all()
    datos = {
        'accesorios' : accesorios
    }
    return render(request, 'mostrar.html', datos)

