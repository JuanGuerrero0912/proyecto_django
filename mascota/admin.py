from django.contrib import admin
from mascota.models import Mascota

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    readonly_fields = ("updated", "fecha_ingreso")

admin.site.register(Mascota, MascotaAdmin)