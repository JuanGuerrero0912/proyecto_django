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
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['tipo_documento'].widget.attrs.update({
         'class': 'form-control',
      })

class Usuario_Administrador(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name']

class Perfil_Administrador(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion']
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['tipo_documento'].widget.attrs.update({
         'class': 'form-control',
      })

class Usuario_Veterinario(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name']

class Perfil_Veterinario(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion']

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['tipo_documento'].widget.attrs.update({
         'class': 'form-control',
      })

class Perfil_Registro(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion', 'rol']

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['rol'].widget.attrs.update({
         'class': 'form-control',
      })

      self.fields['tipo_documento'].widget.attrs.update({
         'class': 'form-control',
      })

class Perfil_Registro_Adoptante(forms.ModelForm):
   class Meta:
      model = Perfil
      fields = ['imagen', 'tipo_documento', 'documento', 'celular', 'ciudad', 'direccion']

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)


      self.fields['tipo_documento'].widget.attrs.update({
         'class': 'form-control',
      })