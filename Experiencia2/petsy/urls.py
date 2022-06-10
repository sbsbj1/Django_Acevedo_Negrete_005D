from django.contrib import admin
from unicodedata import name
from django.urls import path 
from .views import calculadora, Contacto, Feriados, form_accesorio, form_modaccesorio, galeria, index, registracion, somos,mostrar, form_del_accesorio

urlpatterns = [
    path('', index, name="index"),
    path('calculadora', calculadora, name="calculadora"),
    path('Contacto', Contacto, name="Contacto"),
    path('Feriados', Feriados, name="Feriados"),
    path('galeria', galeria, name="galeria"),
    path('registracion', registracion, name="registracion"),
    path('somos', somos, name="somos"),
    path('mostrar/', mostrar, name="mostrar"),
    path('form_accesorio/', form_accesorio, name="form_accesorio"), 
    path('form_modaccesorio/<id>', form_modaccesorio, name="form_modaccesorio"),
    path('form_del_accesorio/<id>', form_del_accesorio, name="form_del_accesorio"),


]