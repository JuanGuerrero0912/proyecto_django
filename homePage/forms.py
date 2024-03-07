from django import forms
from django.contrib.auth.models import User
from login.models import Perfil

class Usuario_Adoptante(forms.ModelForm):
   class Meta:
      model = User
      fields = ['first_name', 'last_name']
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['first_name'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['last_name'].widget.attrs.update({
         'class': 'form-control',
      })


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
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['first_name'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['last_name'].widget.attrs.update({
         'class': 'form-control',
      })

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
   
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      self.fields['first_name'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['last_name'].widget.attrs.update({
         'class': 'form-control',
      })


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
      self.fields['imagen'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['documento'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['celular'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['ciudad'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['direccion'].widget.attrs.update({
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
      self.fields['imagen'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['documento'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['celular'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['ciudad'].widget.attrs.update({
         'class': 'form-control',
      })
      self.fields['direccion'].widget.attrs.update({
         'class': 'form-control',
      })