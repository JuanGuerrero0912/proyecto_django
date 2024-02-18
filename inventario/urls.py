from django.urls import path
from inventario import views

urlpatterns = [
    path('registrar_articulo', views.registrar_articulo, name="Registrar_Articulo"),
    
]