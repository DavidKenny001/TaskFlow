from django import forms
from django.contrib.auth.models import User
from .models import Task

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['titulo', 'descricao', 'prazo', 'prioridade', 'status']