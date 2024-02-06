from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name="Login"),
    path('registro', views.registro, name="Registro"),
]