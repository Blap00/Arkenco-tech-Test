# Shortcuts from Django to render, redirect, etc...
from django.shortcuts import render, redirect

# Decorators, if user is logged or not
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import user_not_authenticated
# Forms

from .models import Usuarios as users
from .forms import *


# Models

# Create your views here.

# Login
@user_not_authenticated
def loginUser(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        def get_username_by_mail(email):
                try:
                    username = users.objects.get(email=email).username
                    return username
                except:
                    username= email
                    return email 
        mutable_data = form.data.copy()
        mutable_data['username'] = get_username_by_mail(form.data["username"])
        form.data = mutable_data
        if form.is_valid():
            
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenido <b>{user.username}</b>! Has iniciado sesión")
                return redirect('../../')
            else:
                pass
        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue                
                messages.error(request, error) 

    form = UserLoginForm()
    return render(
        request=request,
        template_name="Registration/login.html",
        context={"form": form}
        )
# Log Out!
@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('/')
# Index
def home_view(request):
    return render(request,'TechTest/index.html')

# View Usuarios

'''
Realizar un CRUD sobre los usuarios, esto siendo parte del STAFF, ningun otro miembro puede acceder
Si ingresa fuera del rango sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de usuarios registrados en el sistema
Actualizar manualmente cada uno de los usuarios y
Eliminar al usuario que el STAFF seleccione
'''

# View Clientes

'''
Realizar un CRUD sobre los clientes registrados, esto siendo parte del STAFF, ningun otro miembro puede acceder
Si ingresa fuera del rango sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de Clientes registrados en el sistema
Actualizar manualmente cada uno de los Clientes y
Eliminar al cliente que el STAFF seleccione
'''

# View Prospectos

'''
Realizar un CRUD sobre los Prospectos registrados, sin restriccion de acceso.
Si ingresa fuera del rango de ingresado sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de Prospectos registrados en el sistema
Actualizar manualmente cada uno de los Prospectos y
Eliminar el prospecto que se seleccione en base a la id del usuario,
si es STAFF, obtendras todos los prospectos, si no, recibira solamente lo registrado bajo su nombre, con el permiso
de registrar solo bajo su nombre
'''

# View Estados

'''
# revisar si se puede dejar solo a vista del STAFF
Realizar un CRUD sobre los Estados registrados, sin restriccion de acceso.
Si ingresa fuera del rango de ingresado sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de Estados registrados en el sistema
Actualizar manualmente cada uno de los Estados y
Eliminar el prospecto que se seleccione en base a la id del usuario,
si es STAFF, obtendras todos los Estados, si no, recibira solamente lo registrado bajo su nombre, con el permiso
de registrar solo bajo su nombre
'''

# View Etapas
'''
# revisar si se puede dejar solo a vista del STAFF
Realizar un CRUD sobre los Etapas registrados, sin restriccion de acceso.
Si ingresa fuera del rango de ingresado sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de Etapas registrados en el sistema
Actualizar manualmente cada uno de los Etapas y
Eliminar el prospecto que se seleccione en base a la id del usuario,
si es STAFF, obtendras todos los Etapas, si no, recibira solamente lo registrado bajo su nombre, con el permiso
de registrar solo bajo su nombre
'''
# View User & config self
'''
# revisar si se puede dejar solo a vista del STAFF
Realizar un CRUD sobre los Usuario registrados, sin restriccion de acceso.
Si ingresa fuera del rango de ingresado sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de Usuario registrados en el sistema
Actualizar manualmente cada uno de los Usuario y
Eliminar el prospecto que se seleccione en base a la id del usuario,
si es STAFF, obtendras todos los Usuario, si no, recibira solamente lo registrado bajo su nombre, con el permiso
de registrar solo bajo su nombre
'''