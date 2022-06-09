from tabnanny import verbose
from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria


class Accesorio(models.Model):
    idProducto = models.CharField(max_length=8, primary_key=True, verbose_name='Id del Producto')
    clase = models.CharField(max_length=20, verbose_name='Tipo de Mascota')
    stock = models.IntegerField(verbose_name='Stock del producto')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.idProducto
