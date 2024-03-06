from django.db import models
from django.contrib.auth import get_user_model
from .choices import estado_mas, sex, selec_edad, selec_raza, perfil, estado_soli, fase_segui

Usuario = get_user_model()

class Mascota(models.Model):

    nombre = models.CharField(max_length = 50)
    caracteristicas = models.CharField(max_length = 250)
    estadoMascota = models.IntegerField(null = False, blank = False, choices = estado_mas, default= 1)
    sexo = models.IntegerField(null = False, blank = False, choices = sex, default= 1)
    fecha_ingreso = models.DateField(auto_now_add = True)
    edad = models.IntegerField()
    edad_m_a = models.IntegerField(null = False, blank = False, choices = selec_edad, default= 1)
    imagen = models.ImageField(upload_to='mascota/', null = True, blank= True)
    raza = models.IntegerField(null = False, blank = False, choices = selec_raza, default= 1)
    estadoRegistro = models.IntegerField(null = False, blank = False, choices = perfil, default= 1)
    updated = models.DateTimeField(auto_now_add= True)
    administrativo = models.ForeignKey(Usuario, on_delete = models.CASCADE)

    class meta:
        db_table = 'mascota'
        verbose_name=["Mascota"]
        verbose_name_plural=["Mascotas"]
        ordering=['id']
    
    def __str__(self):
        return f'{self.nombre}, fecha de ingreso:   {self.fecha_ingreso}'
    
class Adopcion(models.Model):
    mascota= models.ForeignKey(Mascota, null=True, blank=True, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    fecha_adopcion = models.DateField(auto_now_add = True)
    estado_adopcion = models.IntegerField(null = False, blank = False, choices = perfil, default= 1)
    updated = models.DateTimeField(auto_now_add= True)
    
    class meta:
        db_table = 'adopcion'
        verbose_name=["Adopcion"]
        verbose_name_plural=["Adopciones"]
        ordering=['id']
        
    def __str__(self):
        return f'{self.mascota.nombre} fecha de adopcion: {self.fecha_adopcion}'

class HistorialMedico(models.Model):
    mascota= models.ForeignKey(Mascota, null=True, blank=True, on_delete=models.CASCADE)
    fecha_historial = models.DateField(auto_now_add = True)
    diagnostico = models.FileField(upload_to='historialesMedicos/', verbose_name='Historial Medico', null = False, blank = False)
    estado_historial = models.IntegerField(null = False, blank = False, choices = perfil, default= 1)
    updated = models.DateTimeField(auto_now_add= True)
    veterinario = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    class meta:
        db_table = 'historialMedico'
        verbose_name=["HistorialMedico"]
        verbose_name_plural=["HistorialesMedicos"]
        ordering=['id']
        
    def __str__(self):
        return f'{self.mascota.nombre}'
    
class SolicitudAdopcion(models.Model):
    mascota= models.ForeignKey(Mascota, null=True, blank=True, on_delete=models.CASCADE)
    estado_proceso = models.IntegerField(null = False, blank = False, choices = estado_soli, default= 1)
    fecha_solicitud = models.DateField(auto_now_add = True)
    solicitud = models.FileField(upload_to='solicitudesAdopcion/', verbose_name='Solicitud Adopción', null = False, blank = False)
    estado_solicitud = models.IntegerField(null = False, blank = False, choices = perfil, default= 1)
    updated = models.DateTimeField(auto_now_add= True)
    adoptante = models.ForeignKey(Usuario, on_delete = models.CASCADE)
    class meta:
        db_table = 'solicitudAdopcion'
        verbose_name=["SolicitudAdopcion"]
        verbose_name_plural=["SolicitudesAdopcion"]
        ordering=['id']
        
    def __str__(self):
        return f'{self.mascota.nombre}, fecha de solicitud:   {self.fecha_solicitud}'
    
class SeguimientoAdopcion(models.Model):
    solicitud_adopcion = models.ForeignKey(SolicitudAdopcion, null=True, blank=True, on_delete=models.CASCADE)
    fase = models.IntegerField(null = False, blank = False, choices = fase_segui, default= 1)
    estado_fase = models.IntegerField(null = False, blank = False, choices = estado_soli, default= 1)
    fecha_seguimiento = models.DateField(auto_now_add = True)
    estado_seguimiento = models.IntegerField(null = False, blank = False, choices = perfil, default= 1)
    updated = models.DateTimeField(auto_now_add= True)
    class meta:
        db_table = 'seguimientoadopcion'
        verbose_name=["SeguimientoAdopcion"]
        verbose_name_plural=["SeguimientosAdopcion"]
        ordering=['id']
        
    def __str__(self):
        return f'{self.solicitud_adopcion.mascota.nombre}, fecha de seguimiento:   {self.fecha_seguimiento}'
    
    