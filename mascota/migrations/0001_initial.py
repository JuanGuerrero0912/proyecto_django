# Generated by Django 5.0.2 on 2024-03-06 20:46

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
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('caracteristicas', models.CharField(max_length=250)),
                ('estadoMascota', models.IntegerField(choices=[(1, 'Para Adoptar'), (2, 'En Tratamiento'), (3, 'Adoptado')], default=1)),
                ('sexo', models.IntegerField(choices=[(1, 'Macho'), (2, 'Hembra')], default=1)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('edad', models.IntegerField()),
                ('edad_m_a', models.IntegerField(choices=[(1, 'Meses'), (2, 'Años')], default=1)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='mascota/')),
                ('raza', models.IntegerField(choices=[(1, 'Pastor Aleman'), (2, 'Criollo'), (3, 'Labrador'), (4, 'Golden'), (5, 'Pincher'), (6, 'Otro')], default=1)),
                ('estadoRegistro', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('administrativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_historial', models.DateField(auto_now_add=True)),
                ('diagnostico', models.FileField(upload_to='historialesMedicos/', verbose_name='Historial Medico')),
                ('estado_historial', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('veterinario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='Adopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_adopcion', models.DateField(auto_now_add=True)),
                ('estado_adopcion', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('adoptante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_proceso', models.IntegerField(choices=[(1, 'Aceptada'), (2, 'En Tramite'), (3, 'Rechazada')], default=1)),
                ('fecha_solicitud', models.DateField(auto_now_add=True)),
                ('solicitud', models.FileField(upload_to='solicitudesAdopcion/', verbose_name='Solicitud Adopción')),
                ('estado_solicitud', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('adoptante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='SeguimientoAdopcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fase', models.IntegerField(choices=[(1, 'Fase 1'), (2, 'Fase 2'), (3, 'Fase 3'), (4, 'Terminado')], default=1)),
                ('estado_fase', models.IntegerField(choices=[(1, 'Aceptada'), (2, 'En Tramite'), (3, 'Rechazada')], default=1)),
                ('fecha_seguimiento', models.DateField(auto_now_add=True)),
                ('estado_seguimiento', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('solicitud_adopcion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.solicitudadopcion')),
            ],
        ),
    ]
