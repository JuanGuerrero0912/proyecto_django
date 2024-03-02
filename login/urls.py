from django.urls import path
from login.views import interfaz_login, cerrar_sesion, VRegistro
from django.contrib.auth import views as auth_views
from login import views

urlpatterns = [
    #_______________________________________________________________________________________________
    # Urls Login
    path('', interfaz_login, name="Login"),
    path('registro', VRegistro.as_view(), name="Registro"),
    path('cerrar_sesion', cerrar_sesion, name="Cerrar_Session"),
    path('restablecer_contraseña', auth_views.PasswordResetView.as_view(
        template_name='paginas_login/restablecer_contraseña.html', 
        email_template_name= 'paginas_login/mensaje_email.html'),
        name='password_reset'),
    path('enlace_enviado', auth_views.PasswordResetDoneView.as_view(
        template_name='paginas_login/mensaje_contraseña.html'), 
        name='password_reset_done'),
    path('cambio_contraseña/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='paginas_login/cambiar_contraseña.html'), 
        name='password_reset_confirm'),
    path('contraseña_restablecida', auth_views.PasswordResetCompleteView.as_view(
        template_name='paginas_login/cambio_contraseña_efectuado.html'), 
        name='password_reset_complete'),

    #_______________________________________________________________________________________________
    # Urls Crud Usuarios

    
]