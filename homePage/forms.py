from django import forms
from django.contrib.auth.models import User
from login.models import Perfil

class Usuario_Adoptante(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name']

class Perfil_Adoptante(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion']

class Usuario_Administrador(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name']

class Perfil_Administrador(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion']

class Usuario_Veterinario(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name']

class Perfil_Veterinario(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion']