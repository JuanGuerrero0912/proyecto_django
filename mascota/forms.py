from django import forms
from mascota.models import Mascota, Adopcion, HistorialMedico, SolicitudAdopcion, SeguimientoAdopcion

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'
        exclude = ()

class AdopcionForm(forms.ModelForm):
    class Meta:
        model = Adopcion
        fields = '__all__'
        exclude = ()
        
class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = '__all__'
        exclude = ()
        
class SolicitudAdopcionForm(forms.ModelForm):
    class Meta:
        model = SolicitudAdopcion
        fields = '__all__'
        exclude = ()
        
class SeguimientoAdopcionForm(forms.ModelForm):
    class Meta:
        model = SeguimientoAdopcion
        fields = '__all__'
        exclude = ()