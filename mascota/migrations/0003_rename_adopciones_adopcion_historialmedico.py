# Generated by Django 5.0.2 on 2024-02-16 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_adopciones'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Adopciones',
            new_name='Adopcion',
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_adopcion', models.DateField(auto_now_add=True)),
                ('diagnostico', models.FileField(upload_to='historialesMedicos/', verbose_name='Historial Medico')),
                ('estado_historial', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.mascota')),
            ],
        ),
    ]