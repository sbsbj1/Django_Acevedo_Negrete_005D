from unicodedata import name
from django.urls import path 
from .views import calculadora, Contacto, Feriados, galeria, index, registracion, somos

urlpatterns = [
    path('', index, name="index"),
    path('calculadora', calculadora, name="calculadora"),
    path('Contacto', Contacto, name="Contacto"),
    path('Feriados', Feriados, name="Feriados"),
    path('galeria', galeria, name="galeria"),
    path('registracion', registracion, name="registracion"),
    path('somos', somos, name="somos"),

]