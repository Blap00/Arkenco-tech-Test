# Shortcuts from Django to render, redirect, etc...
from django.shortcuts import render, redirect, get_object_or_404

# Decorators, if user is logged or not
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .decorators import user_not_authenticated
# Forms

from .models import Usuarios as users, cliente 
from .forms import *

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
                return redirect('/')
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

# Registro de usuarios:
def customRegistro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            if(request.user=="AnonymousUser"):
                login(request, user)  # Remove this line
                messages.success(request, f"New account created: {user.username}, succesfully logged")
                return redirect('/')
            elif(request.user.is_staff):
                messages.success(request, f"New account created: {user.username}, succesfully registered")
                return redirect('/usuarios')
            else:
                return redirect('/')
            
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = CustomUserCreationForm()

    return render(
        request=request,
        template_name="registration/registro.html",
        context={"form": form}
    )
# Index
def home_view(request):
    return render(request,'TechTest/index.html')


# View Usuarios
# 08-05-2024
def users_view(request):
    if(request.user.is_staff):
        # Si es Staff muestra todos los usuarios registrados en el sistema
        queryset = users.objects.all().order_by("date_joined")
        context = {
            'Usuarios': queryset,
            }
        return render(request,'TechTest/UsuariosHTML/Usuarios.html', context)
    else:
        return redirect('/')
    
# Update USER
def update_usuario(request, pk):
    user = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        form = UsuariosCrudForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request,f"El usuario {user.username}  ha sido actualizado con éxito.")
            return redirect('/usuarios')
        else:
            messages.error(request,"El formulario no se encuentra completo, porfavor  revise e intente nuevamente.")
    else:
        form = UsuariosCrudForm(instance=user)
    return render(request, 'TechTest/UsuariosHTML/update_usuario.html', {'form': form})

# Delete USER
def delete_usuario(request, pk):
    usuario = get_object_or_404(Usuarios, pk=pk)
    if request.method == 'POST':
        ownPK = request.user.id
        if ownPK==usuario.id:
            messages.error(request,"No puedes eliminar tu propio perfil de usuario.")
            return redirect("/usuarios")
        else:
            messages.success(request,f"Has eliminado a {usuario.username} exitosamente.")
            usuario.delete()
            return redirect('/usuarios')
    return render(request, 'TechTest/UsuariosHTML/delete_usuario.html', {'usuario': usuario})

'''
Realizar un CRUD sobre los usuarios, esto siendo parte del STAFF, ningun otro miembro puede acceder
Si ingresa fuera del rango sera automaticamente redirigido fuera del sitio al index,
Permitira Crear y leer una lista de usuarios registrados en el sistema
Actualizar manualmente cada uno de los usuarios y
Eliminar al usuario que el STAFF seleccione
'''

# View Clientes
# 08-05-2024
def clientes_view(request):
    if(request.user.is_staff):
        # Si es Staff muestra todos los usuarios registrados en el sistema
        queryset = cliente.objects.all().order_by("id_cliente")
        context = {
            'Cliente': queryset,
            }
        return render(request,'TechTest/ClientesHTML/clientes.html', context)
    else:
        return redirect('/')
# Añadir clientes
def clientes_new(request):
    if request.method == 'POST':
        form = ClientesCrudForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"El cliente ha sido creado con éxito.")
            return redirect('/clientes')
        else:
            print(form.errors)
            messages.error(request,"El formulario no se encuentra completo, porfavor revise e intente nuevamente.")
    else:
        form = ClientesCrudForm()
    return render(request, 'TechTest/ClientesHTML/cliente_new.html', {'form': form})
# Update Cliente
def update_cliente(request, pk):
    clientes = get_object_or_404(cliente, pk=pk)
    if request.method == 'POST':
        form = ClientesCrudForm(request.POST, instance=clientes)

        if form.is_valid():
            form.save()
            messages.success(request,f"El cliente {clientes.nombre_empresa}  ha sido actualizado con éxito.")
            return redirect('/clientes')
        else:
            messages.error(request,"El formulario no se encuentra completo, porfavor  revise e intente nuevamente.")
    else:
        form = ClientesCrudForm(instance=clientes)
    return render(request, 'TechTest/ClientesHTML/update_clientes.html', {'form': form})
# Delete Cliente
def delete_cliente(request, pk):

    clientes = get_object_or_404(cliente, pk=pk)
    if request.method == 'POST':
        messages.success(request,f"Has eliminado a {clientes.nombre_empresa} exitosamente.")
        clientes.delete()
        return redirect('/clientes')
    return render(request, 'TechTest/ClientesHTML/delete_cliente.html', {'clientes': clientes})

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