from django.urls import path
from login.views import interfaz_login, cerrar_sesion, VRegistro

urlpatterns = [
    path('', interfaz_login, name="Login"),
    path('registro', VRegistro.as_view(), name="Registro"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_Session"),
]