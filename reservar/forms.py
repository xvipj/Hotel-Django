from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        # campos del modelo
        fields = ('fecha_entrada', 'fecha_salida', 'numero_adultos', 'numero_ninos') 
        # asignar un widgets de fecha a los campos fecha_entrada y fecha_salida
        widgets = {
            # attrs={'type': 'date'} le indica a Django que use el selector de fechas del navegador.
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}), 
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
        }