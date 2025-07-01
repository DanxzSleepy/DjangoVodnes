from django import forms
from .models import ideiasModel


class ideiasForm(forms.ModelForm):
    class Meta:
        model = ideiasModel
        fields = ['nome', 'descricao']