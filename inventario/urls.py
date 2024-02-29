from django.urls import path
from inventario import views

urlpatterns = [
    path('registrar_articulo', views.registrar_articulo.as_view(), name="Registrar_Articulo"),
    path('actualizar_articulo/<int:id>', views.actualizar_articulo.as_view(), name="Actualizar_Articulo"),
    path('ver_articulo/<int:id>', views.ver_articulo, name="Ver_Articulo"),
    path('inhabilitar_articulo/<int:id>', views.inhabilitar_articulo, name="Inhabilitar_Articulo"),
    path('lista_articulos_inhabilitados', views.lista_articulos_inhabilitados, name="Lista_articulos_Inhabilitados"),
    path('habilitar_articulo/<int:id>', views.habilitar_articulo, name="Habilitar_Articulo"),
    path('registrar_entrada', views.registrar_Entrada.as_view(), name="Registrar_Entrada"),
    path('actualizar_entrada/<int:id>', views.actualizar_entrada.as_view(), name="Actualizar_Entrada"),
    path('ver_entrada/<int:id>', views.ver_entrada, name="Ver_Entrada"),
    path('inhabilitar_entrada/<int:id>', views.inhabilitar_entrada, name="Inhabilitar_Entrada"),
    path('lista_entradas_inhabilitadas', views.Lista_entradas_inhabilitadas, name="Lista_entradas_Inhabilitadas"),
    path('habilitar_entrada/<int:id>', views.habilitar_entrada, name="Habilitar_Entrada"),
    path('registrar_salida', views.registrar_salida.as_view(), name="Registrar_Salida"),
    path('actualizar_salida/<int:id>', views.actualizar_salida.as_view(), name="Actualizar_Salida"),
    path('ver_salida/<int:id>', views.ver_salida, name="Ver_Salida"),
    path('inhabilitar_salida/<int:id>', views.inhabilitar_salida, name="Inhabilitar_Salida"),
    path('lista_salidas_inhabilitadas', views.lista_salidas_inhabilitadas, name="Lista_salidas_Inhabilitadas"),
    path('habilitar_salida/<int:id>', views.habilitar_salida, name="Habilitar_Salida"),

    #-------------------------------------------------------------------------------------
        #VETERINARIO: 
    path('registrar_salida_veterinario', views.registrar_salida_veter.as_view(), name="Registrar_Salida_Veterinario"),
    path('ver_salida_veterinario/<int:id>', views.ver_salida_veter, name="Ver_Salida_Veterinario"),
    path('actualizar_salida_veterianrio/<int:id>', views.actualizar_salida_veter.as_view(), name="Actualizar_Salida_Veterinario"),
]