from django.db import models
from django.contrib.auth import get_user_model
from inventario.choices import *

# Create your models here.

Usuario = get_user_model()

class Articulos(models.Model):

    nombre = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 200)
    referencia = models.CharField(max_length = 10, unique = True)
    stock = models.PositiveIntegerField(default = 0)
    estado_articulo = models.IntegerField(null = False, blank = False, choices = estado_art, default= 1)
    usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    fecha_registro = models.DateField(auto_now_add = True)

    class meta:
        db_table = 'articulos'
        verbose_name=["Articulo"]
        verbose_name_plural=["Articulos"]
        ordering=['id']
    
    def __str__(self):
        return f'{self.nombre}'


class Entradas(models.Model):

    fecha_entrada = models.DateField(auto_now_add = True)
    articulo = models.ForeignKey(Articulos, on_delete = models.CASCADE)
    cantidad_entrada = models.PositiveIntegerField(default = 0)
    estado_entrada = models.IntegerField(null = False, blank = False, choices = estado_ent, default= 1)

    class meta:
        db_table = 'entradas'
        verbose_name=["Entrada"]
        verbose_name_plural=["Entradas"]
        ordering=['id']
    
    def __str__(self):
        return f'El dia {self.fecha_entrada}, entraron {self.cantidad_entrada} unidades de {self.articulo.nombre}'



class Salidas(models.Model):

    fecha_salida = models.DateField(auto_now_add = True)
    articulo = models.ForeignKey(Articulos, on_delete = models.CASCADE)
    cantidad_salida = models.PositiveIntegerField(default = 0)
    estado_salida = models.IntegerField(null = False, blank = False, choices = estado_sal, default= 1)

    class meta:
        db_table = 'salidas'
        verbose_name=["Salida"]
        verbose_name_plural=["Salidas"]
        ordering=['id']
    
    def __str__(self):
        return f'El dia {self.fecha_salida}, se consumieron {self.cantidad_salida} unidades de {self.articulo.nombre}'



    

