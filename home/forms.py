from django import forms
from .models import Categoria, Post, Perfil
from django.contrib.auth.models import User

class AutorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

class BusquedaPostForm(forms.Form):
    titulo = forms.CharField(max_length=200, required=False, label="Buscar por título")

    def clean_titulo(self):
        data = self.cleaned_data.get("titulo", "")
        if len(data.strip()) == 0:
            raise forms.ValidationError("El título no puede estar vacío.")
        return data

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["avatar", "biografia"]
