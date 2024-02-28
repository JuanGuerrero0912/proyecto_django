from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from mascota import views
from .views import *

urlpatterns = [
    path('registrar_mascota', views.registrar_mascota.as_view(), name="Registrar_Mascota"),
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
    path('registrar_solicitud', views.registrar_solicitud.as_view(), name="Registrar_Solicitud"),
    path('actualizar_solicitud/<int:id>', views.actualizar_solicitud.as_view(), name="Actualizar_Solicitud"),
    path('inhabilitar_solicitud/<int:id>', views.inhabilitar_solicitud, name="Inhabilitar_Solicitud"),
    path('ver_solicitud/<int:id>', views.ver_solicitud, name="Ver_Solicitud"),
    path('habilitar_solicitud/<int:id>', views.habilitar_solicitud, name="Habilitar_Solicitud"),
    path('registrar_seguimiento', views.registrar_seguimiento.as_view(), name="Registrar_Seguimiento"),
    path('actualizar_seguimiento/<int:id>', views.actualizar_seguimiento.as_view(), name="Actualizar_Seguimiento"),
    path('seguimiento_por_mascota/<int:id>', views.seguimiento_por_perrito, name="Seguimiento_Por_Mascota"),
    path('inhabilitar_seguimiento/<int:id>', views.inhabilitar_seguimiento, name="Inhabilitar_Seguimiento"),
    path('ver_seguimiento/<int:id>', views.ver_seguimiento, name="Ver_Seguimiento"),
    path('habilitar_seguimiento/<int:id>', views.habilitar_seguimiento, name="Habilitar_Seguimiento"),
    path('lista_adopciones_inhabilitadas', views.lista_adopciones_inhabilitadas, name="Lista_adopciones_inhabilitadas"),
    path('lista_historiales_inhabilitadas', views.lista_historiales_inhabilitadas, name="Lista_historiales_inhabilitadas"),
    path('lista_mascotas_inhabilitadas', views.lista_mascotas_inhabilitadas, name="Lista_mascotas_inhabilitadas"),
    path('lista_seguimientos_inhabilitados', views.lista_seguimientos_inhabilitados, name="Lista_seguimientos_inhabilitados"),
    path('lista_solicitudes_inhabilitadas', views.lista_solicitudes_inhabilitadas, name="Lista_solicitudes_inhabilitadas"),
    path('descargar/<str:archivo_nombre>/', views.descargar_archivo, name='descargar_archivo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)