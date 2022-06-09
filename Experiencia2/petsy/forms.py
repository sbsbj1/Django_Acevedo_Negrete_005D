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
        fields = ['idProducto', 'clase', 'stock', 'categoria']
        labels = {
            'idProducto': 'IDProducto',
            'clase': 'Clase',
            'stock': 'Stock',
            'categoria': 'Categoria',
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
            )
        }