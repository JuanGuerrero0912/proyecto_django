from django.urls import path
from donaciones import views

urlpatterns = [
    path('registrar_donacion', views.registrar_donacion.as_view(), name="Registrar_Donacion"),
    path('ver_donacion/<int:id>', views.ver_donacion, name="Ver_Donacion"),
    path('actualizar_donacion/<int:id>', views.actualizar_donacion.as_view(), name="Actualizar_Donacion"),
    path('inhabilitar_donacion/<int:id>', views.inhabilitar_donacion, name="Inhabilitar_Donacion"),
]