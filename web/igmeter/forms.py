from django import forms
from .models import Resultados


class ResultadosForm(forms.ModelForm):
    class Meta:
        model = Resultados
        fields = ['contenido']
