#Typing
from typing import Any
# USUARIOS DJANGO CONTRIB
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.forms import UserChangeForm

# SET FORMS
from django import forms

# Models Default
from .models import Usuarios 
# USER LOGIN
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        username = forms.CharField(widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
            label="Username or Email*")

        password = forms.CharField(widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
# User REGISTER
class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # Add Email field
        self.fields['email'] = forms.EmailField()
        self.fields['email'].label = "Direccion de Email: "
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

        # Add Username field
        self.fields['username'] = forms.CharField()
        self.fields['username'].label = "Nombre de usuario: "
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

        # Add first_name field
        self.fields['first_name'] = forms.CharField()
        self.fields['first_name'].label = "Nombre: "
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})

        # Add last_name field
        self.fields['last_name'] = forms.CharField()
        self.fields['last_name'].label = "Apellido: "
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})

        # Add password1 field
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput)
        self.fields['password1'].label = "Contraseña: "
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})

        # Add password2 field
        self.fields['password2']   = forms.CharField(widget=forms.PasswordInput)
        self.fields['password2'].label = "Repita la contraseña: "
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})

    
    class Meta(UserCreationForm.Meta):
            model=Usuarios
            fields=('email',
            'username', 
            'first_name', 
            'last_name', 
            'password1', 
            'password2')

# CRUD USUARIOS SITE:
class CustomUserChangeForm(UserChangeForm):
    # Define un formulario personalizado basado en UserChangeForm
    class Meta(UserChangeForm.Meta):
        # Especifica metadatos sobre el formulario
        model = Usuarios  # Establece el modelo como Usuarios
        fields = ('username', 'email', 'first_name', 'last_name')  # Especifica los campos a incluir en el formulario

class UsuariosCrudForm(UserChangeForm):
    # Define un formulario para operaciones CRUD de usuarios, heredando de UserChangeForm
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)  # Agrega el campo password1
    password2 = forms.CharField(label="Repita la contraseña", widget=forms.PasswordInput)  # Agrega el campo password2

    class Meta(UserChangeForm.Meta):
        # Especifica metadatos sobre el formulario
        model = Usuarios  # Establece el modelo como Usuarios
        fields = ('username', 'email', 'first_name', 'last_name', 'password')  # Especifica los campos a incluir en el formulario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Personaliza las etiquetas de los campos
        self.fields['username'].label = "Nombre de usuario"  # Establece la etiqueta para el campo username
        self.fields['email'].label = "Dirección de Email"  # Establece la etiqueta para el campo email
        self.fields['first_name'].label = "Nombre"  # Establece la etiqueta para el campo first_name
        self.fields['last_name'].label = "Apellido"  # Establece la etiqueta para el campo last_name

        # Aplica la clase 'form-control' a los widgets del formulario para el estilo
        field_names = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']  # Define los nombres de los campos a actualizar
        for field_name in field_names:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})  # Aplica la clase 'form-control'
