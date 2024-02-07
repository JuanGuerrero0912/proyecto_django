from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

estado_mas = [
    (1 , "Para Adoptar"),
    (2 , "En Tratamiento"),
    (3 , "Adoptado")
]

sex = [
    (1 , "Macho"),
    (2 , "Hembra")
]

selec_edad = [
    (1, "Meses"),
    (2, "Años")
]

selec_raza = [
    (1, "Pastor Aleman"),
    (2, "Criollo"),
    (3, "Labrador"),
    (4, "Golden"),
    (5, "Pincher"),
    (6, "Otro"),
]

perfil = [
    (1, "Activo"),
    (2, "Inactivo")
]


class Mascota(models.Model):

    nombre = models.CharField(max_length = 50)
    caracteristicas = models.CharField(max_length = 250)
    estadoMascota = models.IntegerField(null = False, blank = False, choices = estado_mas, default= 1)
    sexo = models.IntegerField(null = False, blank = False, choices = sex, default= 1)
    fecha_ingreso = models.DateField(auto_now_add = True)
    edad = models.IntegerField()
    edad_m_a = models.IntegerField(null = False, blank = False, choices = selec_edad, default= 1)
    imagen = models.ImageField(upload_to="mascota", null = True, blank= True)
    raza = models.IntegerField(null = False, blank = False, choices = selec_raza, default= 1)
    estado_mascota = models.IntegerField(null = False, blank = False, choices = perfil, default= 1)
    updated = models.DateTimeField(auto_now_add= True)

    class meta:
        db_table = 'mascota'
        verbose_name=["Mascota"]
        verbose_name_plural=["Mascotas"]
        ordering=['id']
    
    def __str__(self):
        return f'{self.nombre} ingreso el {self.fecha_ingreso}"'
    
    
    


    
