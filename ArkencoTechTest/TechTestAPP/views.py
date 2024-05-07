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
        template_name="registration/login.html",
        context={"form": form}
        )
# Index
def home_view(request):
    return render(request,'index.html')