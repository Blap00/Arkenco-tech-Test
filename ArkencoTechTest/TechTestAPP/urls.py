# This file is used to map the URL to the view function
from django.urls import path
from . import views
#from django.contrib.auth.views import LogoutView
#from django.contrib.auth import views as auth_views


app_name = "TechTestAPP"
urlpatterns = [
    path('', views.home_view, name="Home"),
    path('logout', views.custom_logout, name='logout'),
    path('login', views.loginUser, name='login'),
    path('registrar', views.customRegistro, name='registrar'),
    path('usuarios', views.users_view, name='usuarios'),
    path('usuarios/<int:pk>/update/', views.update_usuario, name='update_usuario'),
    path('usuarios/<int:pk>/delete/', views.delete_usuario, name='delete_usuario'),
]