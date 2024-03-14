from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from mascota import views
from .views import *

urlpatterns = [
    path('registrar_mascota', views.registrar_mascota.as_view(), name="Registrar_Mascota"),
    path('video/', views.mostrar_video, name='mostrar_video'),
    path('actualizar_mascota/<int:id>', views.actualizar_mascota.as_view(), name="Actualizar_Mascota"),
    path('inhabilitar_mascota/<int:id>', views.inhabilitar_mascota, name="Inhabilitar_Mascota"),
    path('ver_mascota/<int:id>', views.ver_mascota, name="Ver_Mascota"),
    path('habilitar_mascota/<int:id>', views.habilitar_mascota, name="Habilitar_Mascota"),
    path('registrar_adopcion', views.registrar_adopcion.as_view(), name="Registrar_Adopcion"),
    path('actualizar_adopcion/<int:id>', views.actualizar_adopcion.as_view(), name="Actualizar_Adopcion"),
    path('inhabilitar_adopcion/<int:id>', views.inhabilitar_adopcion, name="Inhabilitar_Adopcion"),
    path('ver_adopcion/<int:id>', views.ver_adopcion, name="Ver_Adopcion"),
    path('habilitar_adopcion/<int:id>', views.habilitar_adopcion, name="Habilitar_Adopcion"),
    path('registrar_historial', views.registrar_historial.as_view(), name="Registrar_Historial"),
    path('actualizar_historial/<int:id>', views.actualizar_historial.as_view(), name="Actualizar_Historial"),
    path('inhabilitar_historial/<int:id>', views.inhabilitar_historial, name="Inhabilitar_Historial"),
    path('ver_historial/<int:id>', views.ver_historial, name="Ver_Historial"),
    path('habilitar_historial/<int:id>', views.habilitar_historial, name="Habilitar_historial"),

    path('historial_por_mascota/<int:id>', views.historiales_medicos_por_perrito, name="Historial_Por_Mascota"),
    path('registrar_historial_por_mascota/<int:id>', views.registrar_historial_medico_por_perrito.as_view(), name="Registrar_Historial_por_mascota"),
    path('actualizar_historial_por_mascota/<int:id>/<int:id_historial>', views.actualizar_historial_por_mascota.as_view(), name="Actualizar_Historial_por_mascota"),
    path('ver_historial_por_mascota/<int:id>/<int:id_historial>', views.ver_historial_por_mascota, name="Ver_Historial_por_mascota"),
    path('lista_historiales_inhabilitadas_por_mascota/<int:id>', views.lista_historiales_inhabilitadas_por_mascota, name="Lista_historiales_inhabilitados_por_mascota"),
    path('inhabilitar_historial_por_mascota/<int:id>', views.inhabilitar_historial_por_mascota, name="Inhabilitar_Historial_por_mascota"),
    path('habilitar_historial_por_mascota/<int:id>', views.habilitar_historial_por_mascota, name="Habilitar_Historial_por_mascota"),

    path('historial_por_mascota/<int:id>', views.historiales_medicos_por_perrito, name="Historial_Por_Mascota"),
    path('registrar_solicitud', views.registrar_solicitud.as_view(), name="Registrar_Solicitud"),
    path('actualizar_solicitud/<int:id>', views.actualizar_solicitud.as_view(), name="Actualizar_Solicitud"),
    path('inhabilitar_solicitud/<int:id>', views.inhabilitar_solicitud, name="Inhabilitar_Solicitud"),
    path('ver_solicitud/<int:id>', views.ver_solicitud, name="Ver_Solicitud"),
    path('habilitar_solicitud/<int:id>', views.habilitar_solicitud, name="Habilitar_Solicitud"),
    path('actualizar_seguimiento/<int:id>', views.actualizar_seguimiento.as_view(), name="Actualizar_Seguimiento"),
    path('seguimiento_por_perrito/<int:id>', views.seguimiento_por_perrito, name="Seguimiento_Por_Mascota"),
    path('inhabilitar_seguimiento/<int:id>', views.inhabilitar_seguimiento, name="Inhabilitar_Seguimiento"),
    path('ver_seguimiento/<int:id>', views.ver_seguimiento, name="Ver_Seguimiento"),
    path('habilitar_seguimiento/<int:id>', views.habilitar_seguimiento, name="Habilitar_Seguimiento"),
    path('lista_adopciones_inhabilitadas', views.lista_adopciones_inhabilitadas, name="Lista_adopciones_inhabilitadas"),
    path('lista_historiales_inhabilitadas', views.lista_historiales_inhabilitadas, name="Lista_historiales_inhabilitadas"),
    path('lista_mascotas_inhabilitadas', views.lista_mascotas_inhabilitadas, name="Lista_mascotas_inhabilitadas"),
    path('lista_seguimientos_inhabilitados', views.lista_seguimientos_inhabilitados, name="Lista_seguimientos_inhabilitados"),
    path('lista_solicitudes_inhabilitadas', views.lista_solicitudes_inhabilitadas, name="Lista_solicitudes_inhabilitadas"),
    path('descargar/<str:archivo_nombre>/', views.descargar_archivo, name='descargar_archivo'),
    
    
    #VETERINARIO
    path('ver_adopcion_vete/<int:id>', views.ver_adopcion_vete, name="Ver_adopcion_vete"),
    path('adopcion_inhabilitada_vete', views.adopcion_inhabilitada_vete, name="Adopcion_inhabilitada_vete"),
    path('registrar_mascota_vete', views.registrar_mascota_vete.as_view(), name="Registrar_mascota_vete"),
    path('actualizar_mascota_vete/<int:id>', views.actualizar_mascota_vete.as_view(), name="Actualizar_mascota_vete"),
    path('inhabilitar_mascota_vet/<int:id>', views.inhabilitar_mascota_vet, name="Inhabilitar_mascota_vet"),
    path('ver_mascota_vet/<int:id>', views.ver_mascota_vet, name="Ver_mascota_vet"),
    path('habilitar_mascota_vet/<int:id>', views.habilitar_mascota_vet, name="Habilitar_mascota_vet"),
    path('lista_mascotas_inhabilitadas_vet', views.lista_mascotas_inhabilitadas_vet, name="Lista_mascotas_inhabilitadas_vet"),
    path('registrar_historial_vete', views.registrar_historial_vete.as_view(), name="Registrar_historial_vete"),
     path('actualizar_historial_vete/<int:id>', views.actualizar_historial_vete.as_view(), name="Actualizar_historial_vete"),
    path('inhabilitar_historial_vete/<int:id>', views.inhabilitar_historial_vete, name="Inhabilitar_historial_vete"),
    path('ver_historial_vete/<int:id>', views.ver_historial_vete, name="Ver_historial_vete"),
    path('habilitar_historial_vete/<int:id>', views.habilitar_historial_vete, name="Habilitar_historial_vete"),
    path('lista_historial_inhabilitado_vet', views.lista_historial_inhabilitado_vet, name="Lista_historial_inhabilitado_vet"),


    path('historiales_medicos_por_perrito_vet/<int:id>', views.historiales_medicos_por_perrito_vet, name="historiales_medicos_por_perrito_vet"),
    path('registrar_historial_por_mascota_veter/<int:id>', views.registrar_historial_medico_por_perrito_veter.as_view(), name="Registrar_Historial_por_mascota_veter"),
    path('actualizar_historial_por_mascota_veter/<int:id>/<int:id_historial>', views.actualizar_historial_por_mascota_veter.as_view(), name="Actualizar_Historial_por_mascota_veter"),
    path('ver_historial_por_mascota_veter/<int:id>/<int:id_historial>', views.ver_historial_por_mascota_veter, name="Ver_Historial_por_mascota_veter"),
    path('inhabilitar_historial_por_mascota_veter/<int:id>', views.inhabilitar_historial_por_mascota_veter, name="Inhabilitar_Historial_por_mascota_veter"),
    path('lista_historial_inhabilitado_por_mascota_veter/<int:id>', views.lista_historiales_inhabilitadas_por_mascota_veter, name="Lista_Historial_Inhabilitados_por_mascota_veter"),
    path('habilitar_historial_por_mascota_veter/<int:id>', views.habilitar_historial_por_mascota_veter, name="Habilitar_Historial_por_mascota_veter"),
    

    path('seguimiento_por_perrito_vet/<int:id>', views.seguimiento_por_perrito_vet, name="seguimiento_por_perrito_vet"),
    
    #ADOPTANTE
    path('solicitud_por_mascota/<int:id>', views.solicitud_por_mascota.as_view(), name="Solicitud_por_mascota_adop"),
    path('historiales_por_mascota_adoptante/<int:id>', views.ver_historiales_por_mascota.as_view(), name="Ver_historiales_por_mascota"),
    path('mis_solicitudes', views.mis_solicitudes.as_view(), name="Mis_solicitudes"),
    path('editar_solicitud_adoptante/<int:id>', views.actualizar_solicitud_de_adoptante.as_view(), name="Editar_solicitud_adoptante"),
    path('mis_seguimientos', views.mis_seguimientos.as_view(), name="Mis_seguimientos"),
    path('mis_adopciones', views.mis_adopciones.as_view(), name="Mis_adopciones"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)