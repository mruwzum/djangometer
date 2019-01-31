from django import forms
from .models import Noticias


class MovieForm(forms.ModelForm):
    class Meta:
        model = Noticias
        fields = ['titulo']
