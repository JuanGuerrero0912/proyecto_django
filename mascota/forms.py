from django import forms
from mascota.models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['estadoRegistro'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['edad_m_a'].widget.attrs.update({
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
        self.fields['administrativo'].widget.attrs.update({
            'class': 'form-control',
        })
        
        

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['mascota'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['adoptante'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_adopcion'].widget.attrs.update({
            'class': 'form-control',
        })
        
class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['mascota'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_historial'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['veterinario'].widget.attrs.update({
            'class': 'form-control',
        })
        
class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = '__all__'
        exclude = ()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['mascota'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_proceso'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['estado_solicitud'].widget.attrs.update({
            'class': 'form-control',
        }) 
        self.fields['adoptante'].widget.attrs.update({
            'class': 'form-control',
        }) 
        
class SeguimientoAdopcionForm(forms.ModelForm):
    class Meta:
        model = SeguimientoAdopcion
        fields = '__all__'
        exclude = ()
        
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
        self.fields['estado_seguimiento'].widget.attrs.update({
            'class': 'form-control',
        }) 