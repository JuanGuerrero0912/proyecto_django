from django import forms
from mascota.models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion
from login.models import Perfil
from django.contrib.auth.models import User

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'caracteristicas', 'estadoMascota', 'sexo',
                   'edad','edad_m_a', 'imagen', 'raza']
        exclude = ['administrativo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['caracteristicas'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['edad'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['edad_m_a'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estadoMascota'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['sexo'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['raza'].widget.attrs.update({
            'class': 'form-control',
        })

        
class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = ['mascota', 'adoptante']
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['mascota'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['adoptante'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['mascota', 'diagnostico']
        exclude = ['veterinario']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['mascota'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['diagnostico'].widget.attrs.update({
            'class': 'form-control',
        })



class Historial_medico_por_mascota(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['diagnostico']
        exclude = ['veterinario', 'mascota']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['diagnostico'].widget.attrs.update({
            'class': 'form-control',
        })

class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['mascota', 'estado_proceso', 'solicitud', 'adoptante']
        exclude = []
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['mascota'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['estado_proceso'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['solicitud'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['adoptante'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        
class SeguimientoAdopcionForm(forms.ModelForm):
    class Meta:
        model = SeguimientoAdopcion
        fields = ['solicitud_adopcion','fase', 'estado_fase']
        exclude = []
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['solicitud_adopcion'].widget.attrs.update({
            'class': 'form-control',
            'required': 'required',
        })
        self.fields['fase'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_fase'].widget.attrs.update({
            'class': 'form-control',
        }) 

class SolicitudAdoptanteForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = ['solicitud']
        exclude = ['adoptante', 'estado_proceso', 'fecha_solicitud', 'estado_solicitud', 'mascota']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['solicitud'].widget.attrs.update({
            'class': 'form-control',
        })

        
