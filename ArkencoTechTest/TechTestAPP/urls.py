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
    # Usuarios CRUD Views
    path('usuarios', views.users_view, name='usuarios'),
    path('usuarios/<int:pk>/update/', views.update_usuario, name='update_usuario'),
    path('usuarios/<int:pk>/delete/', views.delete_usuario, name='delete_usuario'),
    # Clientes CRUD Views
    path('clientes', views.clientes_view, name='clientes'),
    path('clientes/register', views.clientes_new, name='regCliente'),
    path('clientes/<int:pk>/update/', views.update_cliente, name='update_cliente'),
    path('clientes/<int:pk>/delete/', views.delete_cliente, name='delete_cliente'),
    # Prospectos CRUD views
    path('prospectos', views.prospectos_view, name='prospectos'),
    path('prospectos/register', views.prospecto_new, name='regProspecto'),
    path('prospectos/<int:pk>/update/', views.update_prospecto, name='update_prospecto'),
    path('prospectos/<int:pk>/delete/', views.delete_prospecto, name='delete_prospecto'),
    # Estados CRUD views
    path('estados', views.estado_view, name='estados'),
    path('estados/register', views.estado_new, name='regEstado'),
    path('estados/<int:pk>/update/', views.update_estado, name='update_estado'),
    path('estados/<int:pk>/delete/', views.delete_estado, name='delete_estado'),

]