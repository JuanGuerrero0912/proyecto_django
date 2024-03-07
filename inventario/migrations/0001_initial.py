# Generated by Django 5.0.1 on 2024-03-07 09:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=200)),
                ('referencia', models.CharField(max_length=10, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='articulo/')),
                ('estado_articulo', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField(auto_now_add=True)),
                ('cantidad_entrada', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('estado_entrada', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.articulos')),
            ],
        ),
        migrations.CreateModel(
            name='Salidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_salida', models.DateField(auto_now_add=True)),
                ('cantidad_salida', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('estado_salida', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('administrativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.articulos')),
            ],
        ),
    ]
