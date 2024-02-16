from django.db import models
from django.contrib.auth import get_user_model
from inventario.models import Articulos
from donaciones.choices import *

# Create your models here.

Usuario = get_user_model()

class Tipo_Donacion(models.Model):

    tipo_donacion = models.CharField(max_length = 50)
    

    class meta:
        db_table = 'tipodonaciones'
        verbose_name=["TipoDonacion"]
        verbose_name_plural=["TipoDonaciones"]
        ordering=['id']
    
    def __str__(self):
        return f'{self.tipo_donacion}'




class Donaciones(models.Model):
    
    tipo_donacion = models.ForeignKey(Tipo_Donacion,  on_delete = models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    cantidad_donacion = models.PositiveIntegerField(default = 0)
    fecha_donacion = models.DateField(auto_now_add = True)
    Articulos = models.ForeignKey(Articulos,on_delete = models.CASCADE)
    estado_donacion = models.IntegerField(null = False, blank = False, choices = estado_do, default= 1)
    entregado = models.BooleanField(default = False)

    class meta:
        db_table = 'donaciones'
        verbose_name=["Donacion"]
        verbose_name_plural=["Donaciones"]
        ordering=['id']
    
    def __str__(self):
        return f'El dia {self.fecha_donacion}, se recibieron {self.cantidad_donacion} de la referencia {self.Articulos}'
