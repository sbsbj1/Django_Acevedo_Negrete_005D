# Generated by Django 4.0.4 on 2022-06-29 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsy', '0004_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Correo',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Correo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Direccion',
            field=models.CharField(max_length=60, null=True, unique=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Telefono',
            field=models.IntegerField(null=True, unique=True, verbose_name='Telefono'),
        ),
    ]
