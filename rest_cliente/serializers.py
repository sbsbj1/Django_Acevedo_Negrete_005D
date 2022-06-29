from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from petsy.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['Rut_Cliente', 'Nombre', 'Transaciones', 'Correo', 'Telefono', 'Direccion']