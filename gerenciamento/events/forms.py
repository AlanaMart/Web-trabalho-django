from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'titulo',
            'tipo',
            'dataInicial',
            'dataFinal',
            'valor',
            'gratuito',
            'local',
            'horario',
            'cidade',
            'vagas',
        ]
        widgets = {
            'dataInicial': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'dataFinal':forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'horario':forms.TimeInput(attrs={'type':'time'}),
        }