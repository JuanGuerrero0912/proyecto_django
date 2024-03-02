from django.db import models
from django.contrib.auth.models import User
from login.choices import *


# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='ImagenPerfil/', null = True, blank= True, default='ImagenPerfil/icon_perfil.png')
    tipo_documento = models.IntegerField(null = False, blank = False, choices = tipo_doc, default= 1)
    documento = models.CharField(max_length = 20, null = True, blank = True)
    celular = models.CharField(max_length = 20, null = True, blank = True)
    ciudad = models.CharField(max_length = 50, null = True, blank = True)
    direccion = models.CharField(max_length = 100, null = True, blank = True)
    estado_perfil = models.IntegerField(null = False, blank = False, choices = estado, default= 1)
    rol = models.IntegerField(null = False, blank = False, choices = roles, default= 3)

    def __str__(self):
        return f'Perfil de {self.user.username} con el rol de {self.get_rol_display()}'
    
    class meta:
        db_table = 'perfiles'
        verbose_name=["Perfil"]
        verbose_name_plural=["Perfiles"]
        ordering=['id']
    


    


