# Generated by Django 5.0.1 on 2024-03-07 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_alter_articulos_imagen_articulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulos',
            old_name='imagen_articulo',
            new_name='imagen',
        ),
    ]
