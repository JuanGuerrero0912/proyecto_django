from django.urls import path
from inventario import views

urlpatterns = [
    path('registrar_articulo', views.registrar_articulo.as_view(), name="Registrar_Articulo"),
    path('actualizar_articulo/<int:id>', views.actualizar_articulo.as_view(), name="Actualizar_Articulo"),
    path('ver_articulo/<int:id>', views.ver_articulo, name="Ver_Articulo"),
    path('inhabilitar_articulo/<int:id>', views.inhabilitar_articulo, name="Inhabilitar_Articulo"),
    path('registrar_entrada', views.registrar_Entrada.as_view(), name="Registrar_Entrada"),
    path('actualizar_entrada/<int:id>', views.actualizar_entrada.as_view(), name="Actualizar_Entrada"),
    path('ver_entrada/<int:id>', views.ver_entrada, name="Ver_Entrada"),
    path('inhabilitar_entrada/<int:id>', views.inhabilitar_entrada, name="Inhabilitar_Entrada"),
    path('registrar_salida', views.registrar_salida.as_view(), name="Registrar_Salida"),
    path('actualizar_salida/<int:id>', views.actualizar_salida.as_view(), name="Actualizar_Salida"),
    path('ver_salida/<int:id>', views.ver_salida, name="Ver_Salida"),
    path('inhabilitar_salida/<int:id>', views.inhabilitar_salida, name="Inhabilitar_Salida"),
]