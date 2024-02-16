from django.contrib import admin
from donaciones.models import Donaciones, Tipo_Donacion

# Register your models here.

admin.site.register(Donaciones)
admin.site.register(Tipo_Donacion)

