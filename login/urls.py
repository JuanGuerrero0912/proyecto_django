from django.urls import path
from login import views

urlpatterns = [
    path('', views.interfaz_login, name="Login"),
    path('registro', views.registro, name="Registro"),
    path('cerrar_sesion', views.cerrar_sesion, name="Cerrar_Session"),
]