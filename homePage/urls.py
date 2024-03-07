from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from homePage import views


urlpatterns = [
    #_________________________________________________________________________________________________________
    #URLS ADMINISTRADOR
    path('', views.Inicio_Admin, name="Inicio_Admin"),
    path('usuarios', views.Usuarios, name="Usuarios"),
    path('registrar_usuario_administrativo', views.Registrar_usuario_administrativo.as_view(), name="Registrar_usuario"),
    path('actualizar_usuario_administrativo/<int:id>', views.Actualizar_usuario_administrativo.as_view(), name="Actualizar_usuario_administrativo"),
    path('ver_usuario_administrativo/<int:id>', views.ver_usuario_administrativo, name="Ver_usuario_administrativo"),
    path('inhabilitar_usuario_administrativo/<int:id>', views.inhabilitar_usuario, name="Inhabilitar_usuario_administrativo"),
    path('lista_usuarios_inhabilitados', views.lista_usuarios_inhabilitados, name="Lista_usuarios_inhabilitados"),
    path('habilitar_usuario_administrativo/<int:id>', views.habilitar_usuario, name="Habilitar_usuario_administrativo"),
    path('adopciones', views.Adopciones, name="Adopciones"),
    path('lista_adoptantes', views.Lista_adoptantes, name="Lista_adoptantes"),
    path('registrar_adoptante', views.registrar_usuario_adoptante.as_view(), name="Registrar_adoptante"),
    path('actualizar_adoptante/<int:id>', views.Actualizar_adoptante.as_view(), name="Actualizar_adoptante"),
    path('ver_adoptante/<int:id>', views.ver_adoptante, name="Ver_adoptante"),
    path('inhabilitar_adoptante/<int:id>', views.inhabilitar_adoptante, name="Inhabilitar_adoptante"),
    path('lista_adoptantes_inhabilitados', views.lista_adoptantes_inhabilitados, name="Lista_adoptantes_inhabilitados"),
    path('habilitar_adoptante/<int:id>', views.habilitar_adoptante, name="Habilitar_adoptante"),
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
    path('perfil_administrador', views.Actualizar_Perfil_Administrador.as_view(), name="Perfil_Administrador"),
    path('cambio_contraseña_administrador', views.CambioContraseñaAdministrador.as_view(), name="Cambio_Contraseña_Administrador"),

    
    #_________________________________________________________________________________________________________
    #URLS VETERINARIO
    path('inicio_veterinario', views.Inicio_Veterinario, name="Inicio_Veter"),
    path('adopciones_vete', views.Adopciones_vete, name="Adopciones_Vete"),
    path('lista_adopciones_vete', views.Lista_adopciones_vete, name="Lista_adopciones_vete"),
    path('lista_mascotas_vete', views.Lista_mascotas_vete, name="Lista_mascotas_vete"),
    path('lista_historial_vete', views.Lista_historial_vete, name="Lista_historial_vete"),
    path('perritos_vete', views.Perritos_vete, name="Perritos_vete"),
    path('articulos_Veterinario', views.vista_articulos_veterinario, name="Articulos_veterinario"),
    path('inventario_Veterinario', views.inventario_veter, name="Inventario_veterinario"),
    path('salidas_Veterinario', views.vista_salidas_veterinario, name="Salidas_veterinario"),
    path('perfil_veterinario', views.Actualizar_Perfil_Veterinario.as_view(), name="Perfil_Veterinario"),
    path('cambio_contraseña_veterinario', views.CambioContraseñaVeterinario.as_view(), name="Cambio_Contraseña_Veterinario"),

    #_________________________________________________________________________________________________________
    #URLS ADOPTANTE
    path('inicio_Adoptante', views.Inicio_Adoptante, name="Inicio_Adoptante"),
    path('registro_perfil_adoptante', views.VPerfilRegistro.as_view(), name="Registro_Perfil_Adoptante"),
    path('perfil_adoptante', views.Actualizar_Perfil_Adoptante.as_view(), name="Perfil_Adoptante"),
    path('cambio_contraseña_adoptante', views.CambioContraseñaADoptante.as_view(), name="Cambio_Contraseña_Adoptante"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)