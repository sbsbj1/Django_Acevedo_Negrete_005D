from cProfile import label
from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget

from petsy.models import Accesorio, Categoria


class AccesorioForm(forms.ModelForm):

    class Meta:
        model = Accesorio
        fields = ['idProducto', 'clase', 'stock', 'categoria', 'imagen']
        labels = {
            'idProducto': 'IDProducto',
            'clase': 'Clase',
            'stock': 'Stock',
            'categoria': 'Categoria',
            'imagen': 'Imagen'
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={     
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID del Producto',
                    'id': 'ID'
                }
            ),
            'clase': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la clase del Producto',
                    'id': 'clase'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el stock del Producto',
                    'id': 'stock'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs={
                  'class': 'form-control',
                    'id': 'imagen'  
                }
            )
        }