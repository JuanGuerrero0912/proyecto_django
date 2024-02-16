from django.contrib import admin
from .models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "fecha_ingreso")
admin.site.register(Mascota, MascotaAdmin)

class AdopcionAdmin(admin.ModelAdmin):
    readonly_fields= ("updated", "fecha_adopcion")
admin.site.register(Adopcion, AdopcionAdmin)

class HistorialMedicoAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "fecha_historial")
admin.site.register(HistorialMedico, HistorialMedicoAdmin)

class SolicitudAdopcionAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "fecha_solicitud")
admin.site.register(SolicitudAdopcion, SolicitudAdopcionAdmin)

class SeguimientoAdopcionAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "fecha_seguimiento")
admin.site.register(SeguimientoAdopcion, SeguimientoAdopcionAdmin)