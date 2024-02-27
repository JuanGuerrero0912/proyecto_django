from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from mascota import views
from .views import *

urlpatterns = [
    path('registrar_mascota', views.registrar_mascota.as_view(), name="Registrar_Mascota"),
    path('actualizar_mascota/<int:id>', views.actualizar_mascota.as_view(), name="Actualizar_Mascota"),
    path('inhabilitar_mascota/<int:id>', views.inhabilitar_mascota, name="Inhabilitar_Mascota"),
    path('registrar_adopcion', views.registrar_adopcion.as_view(), name="Registrar_Adopcion"),
    path('actualizar_adopcion/<int:id>', views.actualizar_adopcion.as_view(), name="Actualizar_Adopcion"),
    path('inhabilitar_adopcion/<int:id>', views.inhabilitar_adopcion, name="Inhabilitar_Adopcion"),
    path('registrar_historial', views.registrar_historial.as_view(), name="Registrar_Historial"),
    path('actualizar_historial/<int:id>', views.actualizar_historial.as_view(), name="Actualizar_Historial"),
    path('inhabilitar_historial/<int:id>', views.inhabilitar_historial, name="Inhabilitar_Historial"),
    path('registrar_solicitud', views.registrar_solicitud.as_view(), name="Registrar_Solicitud"),
    path('actualizar_solicitud/<int:id>', views.actualizar_solicitud.as_view(), name="Actualizar_Solicitud"),
    path('inhabilitar_solicitud/<int:id>', views.inhabilitar_solicitud, name="Inhabilitar_Solicitud"),
    path('registrar_seguimiento', views.registrar_seguimiento.as_view(), name="Registrar_Seguimiento"),
    path('actualizar_seguimiento/<int:id>', views.actualizar_seguimiento.as_view(), name="Actualizar_Seguimiento"),
    path('inhabilitar_seguimiento/<int:id>', views.inhabilitar_seguimiento, name="Inhabilitar_Seguimiento"),
        path('descargar/<str:archivo_nombre>/', views.descargar_archivo, name='descargar_archivo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)