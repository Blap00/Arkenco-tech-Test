#Typing
from typing import Any
# USUARIOS DJANGO CONTRIB
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth.forms import UserChangeForm

# SET FORMS
from django import forms

# Models Default
from .models import Usuarios, cliente, estado, etapa, prospecto
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


# Clientes Formulario Añadir
class ClientesCrudForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClientesCrudForm, self).__init__(*args, **kwargs)
        # Nombre_Empresa
        self.fields['nombre_empresa'] = forms.CharField()
        self.fields['nombre_empresa'].label ="Nombre de Empresa: "
        self.fields['nombre_empresa'].widget.attrs.update({'class': 'form-control'})
        # RUT
        self.fields['rut'] = forms.CharField()
        self.fields['rut'].label ="Digite RUT: "
        self.fields['rut'].widget.attrs.update({'class': 'form-control', 'id':'id_rut'})
        # Dirección        
        self.fields['direccion'] = forms.CharField()
        self.fields['direccion'].label= "Dirección de cliente: "
        self.fields['direccion'].widget.attrs.update({'class': 'form-control'})
        # Telefono
        self.fields['telefono'] = forms.IntegerField()
        self.fields['telefono'].label ="Ingrese su telefono: "
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
    class Meta:
            model=cliente
            fields=('nombre_empresa',
                    'rut',
                    'direccion',
                    'telefono')

# Prospectos Formulario Añadir
class ProspectosCrudForm(forms.ModelForm):
    class Meta:
        model = prospecto
        fields = ['nombre', 'email', 'telefono', 'sexo', 'cliente_id', 'estado_id', 'etapa_id']
        widgets = {
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'cliente_id': forms.Select(attrs={'class': 'form-control'}),
            'etapa_id': forms.Select(attrs={'class': 'form-control'}),
            'estado_id': forms.Select(attrs={'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProspectosCrudForm, self).__init__(*args, **kwargs)
        # nombre
        self.fields['nombre'] = forms.CharField()
        self.fields['nombre'].label ="Nombre del Prospecto: "
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        # email
        self.fields['email'] = forms.EmailField()
        self.fields['email'].label ="Email del Prospecto: "
        self.fields['email'].widget.attrs.update({'class': 'form-control' })
        # telefono        
        self.fields['telefono'] = forms.IntegerField()
        self.fields['telefono'].label= "Telefono del Prospecto: "
        self.fields['telefono'].widget.attrs.update({'class': 'form-control'})
        # fecha_ingreso
        self.fields['fecha_ingreso'] = forms.DateField(
            label="Ingrese la fecha de ingreso",
            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        )
        # sexo
        choices_sexo =[('', 'Sexo'), ('Male', 'Masculino'), ('Female', 'Femenino')]
        self.fields['sexo'] = forms.ChoiceField(choices=choices_sexo)
        self.fields['sexo'].label ="Sexo del prospecto: "
        self.fields['sexo'].empty_label = "Seleccione el sexo: "
        self.fields['sexo'].widget.attrs.update({'class': 'form-control'})
        # cliente_id
        self.fields['cliente_id'] = forms.ModelChoiceField(
            queryset=cliente.objects.all(),
            empty_label="Seleccione un cliente",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        self.fields['cliente_id'].label = "Cliente del prospecto: "
        # estado_id
        self.fields['estado_id'] = forms.ModelChoiceField(
            queryset=estado.objects.all(),
            empty_label="Seleccione un estado",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        self.fields['estado_id'].label = "Estado del prospecto: "

        # etapa_id
        self.fields['etapa_id'] = forms.ModelChoiceField(
            queryset=etapa.objects.all(),
            empty_label="Seleccione una etapa",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        self.fields['etapa_id'].label = "Etapa del Prospecto: "

# Estado Formulario Añadir
class EstadosCrudForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EstadosCrudForm, self).__init__(*args, **kwargs)
        # Estado
        self.fields['estado'] = forms.CharField()
        self.fields['estado'].label ="Nombre de estado: "
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})

    class Meta:
            model=estado
            fields=('estado',)