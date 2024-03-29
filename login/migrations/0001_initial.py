# Generated by Django 5.0.1 on 2024-03-02 04:46

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
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, default='ImagenPerfil/icon_perfil.png', null=True, upload_to='ImagenPerfil/')),
                ('tipo_documento', models.IntegerField(choices=[(1, 'CC'), (2, 'TI'), (3, 'CE'), (4, 'PA')], default=1)),
                ('documento', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('estado_perfil', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('rol', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Veterinario'), (3, 'Adoptante')], default=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
