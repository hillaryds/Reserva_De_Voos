from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label='Email')

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'cpf', 'email', 'data_nascimento', 'senha']