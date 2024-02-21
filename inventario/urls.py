from django.urls import path
from inventario import views

urlpatterns = [
    path('registrar_articulo', views.registrar_articulo.as_view(), name="Registrar_Articulo"),
    path('actualizar_articulo/<int:id>', views.actualizar_articulo.as_view(), name="Actualizar_Articulo"),
    path('inhabilitar_articulo/<int:id>', views.inhabilitar_articulo, name="Inhabilitar_Articulo"),
]