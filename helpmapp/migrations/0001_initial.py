# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('nombreUsuario', models.CharField(default='-', primary_key=True, max_length=12, serialize=False)),
                ('contrasena', models.CharField(default='-', max_length=15)),
                ('correo', models.EmailField(default='-', max_length=254)),
                ('tipo', models.IntegerField(default=1)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CambioInventario',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tipo', models.IntegerField(default=1)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=6, decimal_places=2)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(default='-', max_length=30)),
                ('unidad', models.CharField(default='-', max_length=20)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='CentroDeAcopio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombreUPC', models.CharField(default='-', max_length=30)),
                ('direccion', models.CharField(default='-', max_length=100)),
                ('latitud', models.DecimalField(default=0.0, max_digits=15, decimal_places=10)),
                ('longitud', models.DecimalField(default=0.0, max_digits=15, decimal_places=10)),
                ('provincia', models.CharField(default='-', max_length=30)),
                ('canton', models.CharField(default='-', max_length=30)),
                ('estado', models.IntegerField(default=1)),
                ('almacenamientoAgua', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('almacenamientoRopa', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('almacenamientoComida', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='-', max_length=20)),
                ('estado', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='HelpMapper',
            fields=[
                ('nombre', models.CharField(default='-', max_length=100)),
                ('apellido', models.CharField(default='-', max_length=100)),
                ('nombreUsuario', models.CharField(default='-', primary_key=True, max_length=12, serialize=False)),
                ('contrasena', models.CharField(default='-', max_length=15)),
                ('sexo', models.CharField(default='-', max_length=10)),
                ('cedula', models.CharField(default='-', max_length=10)),
                ('tipoSangre', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=5)),
                ('telefono', models.CharField(default='-', max_length=10)),
                ('correo', models.EmailField(max_length=100)),
                ('estado', models.IntegerField(default=1)),
                ('idHabilidad', models.ForeignKey(default=0, to='helpmapp.Habilidad')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(default='-', max_length=30)),
                ('cantidad', models.DecimalField(default=0.0, max_digits=8, decimal_places=2)),
                ('estado', models.IntegerField(default=1)),
                ('idCategoria', models.ForeignKey(default=0, to='helpmapp.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='cambioinventario',
            name='idProducto',
            field=models.ForeignKey(default=0, to='helpmapp.Producto'),
        ),
        migrations.AddField(
            model_name='administrador',
            name='idCentro',
            field=models.ForeignKey(default=0, to='helpmapp.CentroDeAcopio'),
        ),
    ]
