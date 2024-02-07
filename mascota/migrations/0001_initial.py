# Generated by Django 5.0.1 on 2024-02-07 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('caracteristicas', models.CharField(max_length=250)),
                ('estadoMascota', models.IntegerField(choices=[(1, 'Para Adoptar'), (2, 'En Tratamiento'), (3, 'Adoptado')], default=1)),
                ('sexo', models.IntegerField(choices=[(1, 'M'), (2, 'F')], default=1)),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('edad', models.IntegerField()),
                ('edad_m_a', models.IntegerField(choices=[(1, 'Meses'), (2, 'Años')], default=1)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='mascota')),
                ('raza', models.IntegerField(choices=[(1, 'Macho'), (2, 'Hembra')], default=1)),
                ('estado_mascota', models.IntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
