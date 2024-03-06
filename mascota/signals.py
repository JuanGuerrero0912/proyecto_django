from mascota.models import SolicitudAdopcion, SeguimientoAdopcion
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender= SolicitudAdopcion)
def crear_seguimiento(sender, instance, created, **kwargs): 
    if created : 
        SeguimientoAdopcion.objects.create(solicitud_adopcion=instance)