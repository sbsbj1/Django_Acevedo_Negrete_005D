from django.contrib import admin

from django.contrib import admin
from petsy.models import Accesorio, Categoria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Accesorio)