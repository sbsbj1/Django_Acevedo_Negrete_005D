from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators import csrf

from .forms import AccesorioForm

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


def form_accesorio(request): 

    if request.method=='POST':
        accesorio_form = AccesorioForm(request.POST)
        if accesorio_form.is_valid():
            accesorio_form.save()
            return redirect ('index')
    else:
        accesorio_form = AccesorioForm()
    return render(request, 'crearAccesorios.html', {'accesorio_form': accesorio_form})


def form_modaccesorio(request, id):
    accesorio = Accesorio.objects.get(idProducto=id)
    datos = {
        'form': AccesorioForm(instance = accesorio)
    }
    if request.method=='POST':
        formulario = AccesorioForm(data=request.POST, instance = accesorio)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
        
    return render(request, 'form_modaccesorio.html', datos)

def form_del_accesorio(request,id):
    accesorio = Accesorio.objects.get(idProducto=id)
    accesorio.delete()
    return redirect('mostrar')

