from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homePage import views

urlpatterns = [
    path('', views.Inicio_Admin, name="Inicio_Admin"),
    path('usuarios', views.Usuarios, name="Usuarios"),
    path('adopciones', views.Adopciones, name="Adopciones"),
    path('lista_adoptantes', views.Lista_adoptantes, name="Lista_adoptantes"),
    path('lista_adopciones', views.Lista_adopciones, name="Lista_adopciones"),
    path('lista_usuarios', views.Lista_usuarios, name="Lista_usuarios"),
    path('lista_mascotas', views.Lista_mascotas, name="Lista_mascotas"),
    path('lista_historial_medico', views.Lista_historial_medico, name="Lista_historial_medico"),
    path('lista_solicitudes_adopcion', views.Lista_solicitudes_adopcion, name="Lista_solicitudes_adopcion"),
    path('lista_seguimientos_proceso', views.Lista_seguimientos_proceso, name="Lista_seguimientos_proceso"),
    path('lista_donaciones', views.Lista_donaciones, name="Lista_donaciones"),
    path('lista_articulos', views.Lista_articulos, name="Lista_articulos"),
    path('lista_entradas', views.Lista_entradas, name="Lista_entradas"),
    path('lista_salidas', views.Lista_salidas, name="Lista_salidas"),
    path('inventario', views.Inventario, name="Inventario"),
    path('donaciones', views.Donaciones_Interfaz, name="Donaciones"),
    path('perritos_admin', views.Perritos_admin, name="Perritos_admin"),
    path('inicio_veterinario', views.Inicio_Veterinario, name="Inicio_Veter"),
    path('inicio_Adoptante', views.Inicio_Adoptante, name="Inicio_Adoptante"),

    
]