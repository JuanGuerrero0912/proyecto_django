from django.contrib import admin
from inventario.models import Articulos, Entradas, Salidas
# Register your models here.

admin.site.register(Articulos)
admin.site.register(Entradas)
admin.site.register(Salidas)
