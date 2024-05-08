#Typing
from typing import Any
# USUARIOS DJANGO CONTRIB
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm

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
class UsuariosCrudForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Accede al objeto de solicitud dentro del método __init__
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        
        # Add Username field
        self.fields['username'] = forms.CharField()
        self.fields['username'].label = "Nombre de usuario: "
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

        # Add password1 field
        self.fields['password1'] = forms.CharField(widget=forms.PasswordInput)
        self.fields['password1'].label = "Contraseña: "
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})

        # Add password2 field
        self.fields['password2'] = forms.CharField(widget=forms.PasswordInput)
        self.fields['password2'].label = "Repita la contraseña: "
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    
    class Meta(UserCreationForm.Meta):
        model = Usuarios
        fields = ('username', 'password1', 'password2')
