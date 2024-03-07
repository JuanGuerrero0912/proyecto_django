from django import forms
from mascota.models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion

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
        })
        self.fields['adoptante'].widget.attrs.update({
            'class': 'form-control',
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
        })
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
        })
        self.fields['estado_proceso'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['solicitud'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['adoptante'].widget.attrs.update({
            'class': 'form-control',
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
        })
        self.fields['fase'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_fase'].widget.attrs.update({
            'class': 'form-control',
        }) 
