from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, usuario, nombres, apellidos, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        user = self.model(
            usuario = usuario,
            email = self.normalize_email(email),
            nombres = nombres,
            apellidos = apellidos
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, usuario, nombres, apellidos, password):

        user = self.create_user(
            email,
            usuario = usuario,
            nombres= nombres,
            apellidos=apellidos,
            password = password
        )

        user.usuario_administrador = True
        user.save()
        return user


tipo_doc = [
    (1 , "CC"),
    (2 , "TI"),
    (3 , "CE")
]

perfil = [
    (1, "Activo"),
    (2, "Inactivo")
]

roles = [
    (1 , "Administrador"),
    (2 , "Veterinario"),
    (3 , "Adoptante")
]


# Create your models here.
class Usuario(AbstractBaseUser):
    usuario = models.CharField('Nombre de usuario', unique = True, max_length=100)
    email = models.EmailField("Correo electronico", max_length=254, unique=True)
    nombres = models.CharField('Nombres', max_length=100, blank = True, null = True)
    apellidos = models.CharField('Apellidos', max_length=100, blank = True, null = True)
    tipo_documento = models.IntegerField(null = True, blank = True, choices = tipo_doc, default= 1)
    documento = models.CharField(max_length=12, blank = True, null = True)
    celular = models.CharField(max_length=10, blank = True, null = True)
    ciudad = models.CharField(max_length=100, blank = True, null = True)
    direccion = models.CharField(max_length=100, blank = True, null = True)
    estado = models.IntegerField(null = True, blank = True, choices = perfil, default= 1)
    rol = models.IntegerField(null = True, blank = True, choices = roles, default= 3)

    imagen = models.ImageField('Imagen de perfil', upload_to='ImagenPerfil', max_length=200, blank = True, null = True)
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
    def has_perm(self,perm,ob = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
    